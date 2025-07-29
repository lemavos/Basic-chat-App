""" remove every .pyc file in the project directory """
import os 

BASE_DIR = "."

def remove_cache():
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith(".pyc"):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Removed: {file_path}")
                except Exception as e:
                    print(f"Error removing {file_path}: {e}")