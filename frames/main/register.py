from customtkinter import *
from frames.main.utils import *

def show_register_root(root, show_root):
    frame = CTkFrame(root)

    texto = CTkLabel(frame,text="Create Account", font=("Arial", 18, "bold"))
    texto.pack(padx=10,pady=10)

    username = CTkEntry(frame, height=30, width=200,placeholder_text="insert your username") 
    username.pack(padx=10, pady=10)

    email = CTkEntry(frame, height=30, width=200,placeholder_text="insert your email") 
    email.pack(padx=10, pady=10)

    password = CTkEntry(frame,show="*", height=30, width=200,placeholder_text="insert your password")
    password.pack(padx=10,pady=10)

    checkbox_var = IntVar()  
    show_password = CTkCheckBox(frame, text="Show Password", variable=checkbox_var)
    show_password.pack(padx=10,pady=10)

    error_label = CTkLabel(frame, text="", text_color="red") 
    error_label.pack(padx=10, pady=10)

    botao = CTkButton(frame, text="Register", command=lambda: newUser(username, email, password, error_label))
    botao.pack(padx=10, pady=10)

    botao = CTkButton(frame,
        text="Already have a account? Click to login", 
        command=lambda: show_root("login"),
        fg_color="transparent",
        hover_color="#333333",
        height=30,
        width=200)
    botao.pack(padx=10,pady=10)
    
    checkbox_update(checkbox_var, password, root)
    
    return frame