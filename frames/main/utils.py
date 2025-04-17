import json
import os
from customtkinter import *

# Configurações de caminhos
BASE_DIR = "."
USERS_FILE = os.path.join("server", "users.json")
LOCAL_USER_FILE = os.path.join("data", "local_user.json")
CONFIGURES_FILE = os.path.join("frames", "configures", "configures.json")

# Cores padrão para os temas
COLORS = {
    "dark": {
        "bg": "#242424",
        "text": "white",
        "button": "#1f6aa5",
        "frame": "#2b2b2b"
    },
    "light": {
        "bg": "#f0f0f0",
        "text": "black",
        "button": "#3b8ed0", 
        "frame": "#ffffff"
    }
}

def ensure_data_dir():
    """Garante que os diretórios necessários existam"""
    os.makedirs("data", exist_ok=True)
    os.makedirs("server", exist_ok=True)
    os.makedirs("frames/configures", exist_ok=True)

def read_users():
    """Lê os usuários do arquivo JSON"""
    ensure_data_dir()
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w") as f:
            json.dump({}, f)
        return {}
    
    try:
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}

def save_user(users):
    """Salva os usuários no arquivo JSON"""
    ensure_data_dir()
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

def save_local_user(email, username):
    """Salva os dados do usuário localmente"""
    ensure_data_dir()
    with open(LOCAL_USER_FILE, "w") as f:
        json.dump({"email": email, "username": username}, f, indent=4)

def get_local_user():
    """Obtém os dados do usuário local"""
    if os.path.exists(LOCAL_USER_FILE):
        with open(LOCAL_USER_FILE, "r") as f:
            return json.load(f)
    return None

def get_current_theme():
    """Obtém o tema atual do sistema"""
    try:
        if os.path.exists(CONFIGURES_FILE):
            with open(CONFIGURES_FILE, "r") as f:
                config = json.load(f)
                return config.get("color_theme", "light")
    except Exception as e:
        print(f"Error reading theme config: {e}")
    return "light"

def update_widget_colors(widget, theme=None):
    """
    Atualiza recursivamente as cores de todos os widgets filhos
    Args:
        widget: O widget raiz para atualizar
        theme: "light" ou "dark" (None para usar o tema atual)
    """
    if theme is None:
        theme = get_current_theme()
    
    colors = COLORS[theme]
    
    try:
        if isinstance(widget, (CTkLabel, CTkButton, CTkEntry, CTkComboBox)):
            widget.configure(text_color=colors["text"])
            if isinstance(widget, (CTkButton, CTkComboBox)):
                widget.configure(fg_color=colors["button"])
        
        if isinstance(widget, CTkFrame):
            widget.configure(fg_color=colors["frame"])
    except Exception as e:
        print(f"Error updating widget colors: {e}")
    
    for child in widget.winfo_children():
        update_widget_colors(child, theme)

def newUser(username_entry, email_entry, password_entry, error_label):
    """Registra um novo usuário"""
    username = username_entry.get().strip()
    email = email_entry.get().strip().lower()
    password = password_entry.get().strip()

    error_label.configure(text="")
    
    # Validações
    if not all([username, email, password]):
        error_label.configure(text="All fields are required", text_color="red")
        return False
    
    if "@" not in email or "." not in email:
        error_label.configure(text="Invalid email format", text_color="red")
        return False
    
    if len(password) < 8:
        error_label.configure(text="Password must be at least 8 characters", text_color="red")
        return False
    
    users = read_users()
    
    if email in users:
        error_label.configure(text="Email already registered", text_color="red")
        return False
    
    # Adiciona novo usuário
    users[email] = {
        "username": username,
        "password": password
    }
    
    save_user(users)
    error_label.configure(text="Registration successful!", text_color="green")
    return True

def login(email_entry, password_entry, error_label):
    """Realiza o login do usuário"""
    email = email_entry.get().strip().lower()
    password = password_entry.get().strip()

    if not email or not password:
        error_label.configure(text="Email and password are required", text_color="red")
        return False
    
    users = read_users()
    
    if email not in users:
        error_label.configure(text="Email not found", text_color="red")
        return False
    
    if users[email]["password"] != password:
        error_label.configure(text="Incorrect password", text_color="red")
        return False
    
    save_local_user(email, users[email]["username"])
    error_label.configure(text="")
    return True

def checkbox_update(checkbox_var, password_entry, root):
    """Alterna a visibilidade da senha"""
    if checkbox_var.get() == 1:
        password_entry.configure(show="")
    else:
        password_entry.configure(show="*")
    root.after(100, lambda: checkbox_update(checkbox_var, password_entry, root))

def receive_messages(client_socket, text_widget=None):
    """Recebe mensagens do servidor"""
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break
                
            if text_widget:
                text_widget.insert(END, f"\n{message}")
                text_widget.see(END)
            else:
                print(f"Received: {message}")
                
        except ConnectionResetError:
            if text_widget:
                text_widget.insert(END, "\nConnection lost with server")
            break
        except Exception as e:
            print(f"Error receiving message: {e}")
            break
        
def remove_cache():
    """Remove arquivos de cache (.pyc)"""
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith(".pyc"):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Removed: {file_path}")
                except Exception as e:
                    print(f"Error removing {file_path}: {e}")

def apply_theme(root, theme=None):
    """Aplica o tema a toda a aplicação"""
    if theme is None:
        theme = get_current_theme()
    
    set_appearance_mode(theme)
    update_widget_colors(root, theme)
    root.update()