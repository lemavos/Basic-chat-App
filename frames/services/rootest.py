from customtkinter import *
from frames.main.utils import *

def show_test_root(root, show_root):
    frame = CTkFrame(root)
    
    texto = CTkLabel(frame, text="Isso e um teste")
    texto.pack(padx=10, pady=(20,10))
    
    
    login_button = CTkButton(frame, 
    text="volta pro lobby", 
    command=lambda: show_root("lobby"), 
    height=35, width=120)
    login_button.pack(pady=10)
    
    return frame