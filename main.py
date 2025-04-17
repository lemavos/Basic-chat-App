from customtkinter import *
from frames.main.login import show_login_root
from frames.main.register import show_register_root
from frames.main.lobby import show_lobby_root
from frames.services.chat import show_chat_root
from frames.services.configures import show_configures_root
from frames.services.rootest import show_test_root
from frames.configures.theme_configure import show_theme_configure_root, get_color_theme

def show_root(root, frames, current_frame):
    if current_frame[0]:
        current_frame[0].pack_forget()
    
    current_frame[0] = frames[root]
    current_frame[0].pack(fill="both", expand=True, padx=20, pady=20)

def main():
    root = CTk()
    root.title("Meu App")
    root.geometry("600x500")
    
    # Configura tema inicial
    initial_theme = get_color_theme()
    set_appearance_mode(initial_theme)
    set_default_color_theme("blue")
    
    current_frame = [None]
    frames = {
        "login": show_login_root(root, lambda r: show_root(r, frames, current_frame)),
        "register": show_register_root(root, lambda r: show_root(r, frames, current_frame)),
        "lobby": show_lobby_root(root, lambda r: show_root(r, frames, current_frame)),
        "chat": show_chat_root(root, lambda r: show_root(r, frames, current_frame)),
        "test": show_test_root(root, lambda r: show_root(r, frames, current_frame)),
        "configures": show_configures_root(root, lambda r: show_root(r, frames, current_frame)),
        "change_theme": show_theme_configure_root(root, lambda r: show_root(r, frames, current_frame)),
    }
    
    show_root("login", frames, current_frame)
    root.mainloop()

if __name__ == "__main__":
    main()