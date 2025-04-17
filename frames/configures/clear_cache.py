import os 

pasta_raiz = "."

def remove_cache():
    for root, dirs, files in os.walk(pasta_raiz):
        for file in files:
            if file.endswith(".pyc"):
                caminho_arquivo = os.path.join(root, file)
                os.remove(caminho_arquivo)
                print(f"Arquivo removido: {caminho_arquivo}")