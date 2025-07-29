from customtkinter import *
from app.frames.theme_configure import show_theme_configure_root
from app.services.clear_cache import remove_cache

def show_configures_root(root, show_root):
    frame = CTkFrame(root, fg_color="transparent")
    
    title = CTkLabel(
        frame, 
        text="Configurations",
        font=("Arial", 16, "bold")
    )
    title.pack(padx=10, pady=(20, 10))
    
    buttons = [
        ("Change app theme", lambda: show_root("change_theme")),
        ("Remove cache", remove_cache),
        ("Back to lobby", lambda: show_root("lobby")),
        ("Log out", lambda: show_root("login"), {"fg_color": "red", "hover_color": "#8B0000"}),
    ]
    
    for text, command, *options in buttons:
        button = CTkButton(
            frame, 
            text=text, 
            command=command,
            height=35,
            width=200,
            font=("Arial", 12,"bold"),
            **(options[0] if options else {})
        )
        button.pack(pady=10)
    
    return frame