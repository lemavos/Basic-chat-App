from customtkinter import *
from frames.main.utils import *
import socket
import threading
import json
import os

HOST = "127.0.0.1"
PORT = 5000
LOCAL_USER_FILE = os.path.join("data", "local_user.json")

def get_username():
    #Obtém o username do arquivo local_user.json
    try:
        if os.path.exists(LOCAL_USER_FILE):
            with open(LOCAL_USER_FILE, "r") as f:
                user_data = json.load(f)
                return user_data.get("username", "Anonymous")
    except Exception as e:
        print(f"error to read user data: {e}")
    return "Anonymous"

def show_chat_root(root, show_root):
    frame = CTkFrame(root)
    
    try:
        chat = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        chat.connect((HOST, PORT))
    except Exception as e:
        error_label = CTkLabel(frame, text=f"conection error: {e}", text_color="red")
        error_label.pack(pady=20)
        back_button = CTkButton(frame, text="back to lobby", command=lambda: show_root("lobby"))
        back_button.pack(pady=10)
        return frame
    
    messages_area = CTkTextbox(frame, height=300, width=400, wrap=WORD)
    messages_area.configure(state="disabled")  # Desabilita edição inicialmente
    messages_area.pack(padx=10, pady=10, fill=BOTH, expand=True)
    
    message_entry = CTkEntry(frame, height=30, width=200, placeholder_text="Digite algo...")
    message_entry.pack(padx=10, pady=10, side=LEFT, fill=X, expand=True)
    
    back_button = CTkButton(frame, height=30, width=15, text="Return to lobby", command=lambda: show_root("lobby"))
    back_button.pack(padx=10, pady=10, side=RIGHT)
    
    send_button = CTkButton(frame, text="Enviar", command=lambda: send_message(message_entry, chat, messages_area, get_username()))
    send_button.pack(padx=10, pady=10, side=RIGHT)
    
    
    # msg de erro
    messages_area.tag_config("error", foreground="red")
    
    def receive_messages():
        while True:
            try:
                message = chat.recv(1024).decode("utf-8")
                if message:
                    messages_area.configure(state="normal")
                    messages_area.insert(END, f"{message}\n")
                    messages_area.configure(state="disabled")
                    messages_area.see(END)
            except Exception as e:
                messages_area.configure(state="normal")
                messages_area.insert(END, f"[ERRO] {str(e)}\n", "error")
                messages_area.configure(state="disabled")
                messages_area.see(END)
                break
    
    thread = threading.Thread(target=receive_messages, daemon=True)
    thread.start()
    
    return frame

def send_message(entry, chat_socket, text_widget=None, username="Anonymous"):
    message = entry.get()
    if message:
        try:
            full_message = f"{username}: {message}"
            chat_socket.send(full_message.encode("utf-8"))
            entry.delete(0, END)
            if text_widget:
                text_widget.configure(state="normal")
                text_widget.insert(END, f"You: {message}\n")
                text_widget.configure(state="disabled")
                text_widget.see(END)
        except Exception as e:
            if text_widget:
                text_widget.configure(state="normal")
                text_widget.insert(END, f"[ERRO] error to send: {str(e)}\n", "error")
                text_widget.configure(state="disabled")
                text_widget.see(END)
            print(f"error to send: {e}")