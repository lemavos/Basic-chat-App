from customtkinter import *
from frames.main.utils import *

def show_login_root(root, show_root):
    frame = CTkFrame(root)
    
    texto = CTkLabel(frame, text="Login", font=("Arial", 18, "bold"))
    texto.pack(padx=10, pady=(20,10))

    email = CTkEntry(frame, height=40, width=250, placeholder_text="Insert your email")
    email.pack(padx=10, pady=10, fill="x")

    password = CTkEntry(frame, show="*", height=40, width=250, placeholder_text="Insert your password")
    password.pack(padx=10, pady=10, fill="x")
    
    checkbox_var = IntVar()  
    show_password = CTkCheckBox(frame, text="Show Password", variable=checkbox_var)
    show_password.pack(padx=10, pady=5)

    error_label = CTkLabel(frame, text="", text_color="red", height=20)
    error_label.pack(padx=10, pady=5)

    def attempt_login():
        if login(email, password, error_label):
            show_root("lobby")
    
    login_button = CTkButton(frame, text="Login", command=attempt_login, height=35, width=120)
    login_button.pack(pady=10)
    
    register_button = CTkButton(frame, 
        text="Don't have an account? Create one",
        command=lambda: show_root("register"),
        fg_color="transparent",
        hover_color="#333333",
        height=30,
        width=200)
    register_button.pack(pady=5)

    checkbox_update(checkbox_var, password, root)

    return frame