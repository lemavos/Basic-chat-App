from customtkinter import *
from app.services.utils import *
                
def show_lobby_root(root, show_root):
    frame = CTkFrame(root)
    
    title = CTkLabel(
        frame, 
        text="Lobby\n\nChoose a service",
        font=("Arial", 16, "bold")
    )
    title.pack(padx=10, pady=(20, 10))
    
    buttons = [
        ("chat", lambda: show_root("chat")),
        ("test", lambda: show_root("test")),
        ("Configures", lambda: show_root("configures")),
    ]
    
    for text, command, *options in buttons:
        button = CTkButton(
            frame, 
            text=text, 
            command=command,
            height=35,
            width=200,
            font=("Arial", 12, "bold"),
            **(options[0] if options else {})
        )
        button.pack(pady=10)
    
    return frame