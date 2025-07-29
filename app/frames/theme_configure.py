import os
import json
from customtkinter import *
from app.services.utils import update_widget_colors

CONFIGURES_FILE = os.path.join("frames", "configures", "configures.json")

def get_color_theme():
    try:
        if os.path.exists(CONFIGURES_FILE):
            with open(CONFIGURES_FILE, "r") as f:
                user_data = json.load(f)
                return user_data.get("color_theme", "light")
    except Exception as e:
        print(f"Error reading user data: {e}")
    return "light"

def open_configures():
    if not os.path.exists("frames/configures"):
        os.makedirs("frames/configures")
    
    if not os.path.exists(CONFIGURES_FILE):
        with open(CONFIGURES_FILE, "w", encoding="utf-8") as f:
            json.dump({"color_theme": "light"}, f, ensure_ascii=False, indent=4)
        return {"color_theme": "light"}
    
    try:
        with open(CONFIGURES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return {"color_theme": "light"}

def change_theme_config(frame, root):
    color_theme = theme.get()
    
    with open(CONFIGURES_FILE, "w", encoding="utf-8") as f:
        json.dump({"color_theme": color_theme}, f, ensure_ascii=False, indent=4)
    
    set_appearance_mode(color_theme)
    update_widget_colors(frame, color_theme)
    root.update()

def show_theme_configure_root(root, show_root):
    configures = open_configures()
    color_theme = configures.get("color_theme", "light")
    
    frame = CTkFrame(root, fg_color="transparent")
    
    title = CTkLabel(
        frame, 
        text="Theme Configuration",
        font=("Arial", 16, "bold")
    )
    title.pack(padx=10, pady=(20, 10))

    themes = ["light", "dark"]
    
    global theme
    theme = CTkComboBox(
        frame, 
        values=themes, 
        width=200,
        height=35,
        font=("Arial", 12),
        dropdown_font=("Arial", 12),
        command=lambda _: change_theme_config(frame, root)
    )
    theme.set(color_theme)
    theme.pack(padx=10, pady=(10, 20))

    back_button = CTkButton(
        frame,
        text="Back to Config",
        command=lambda: show_root("configures"),
        height=35,
        width=200,
        font=("Arial", 12)
    )
    back_button.pack(pady=10)

    return frame