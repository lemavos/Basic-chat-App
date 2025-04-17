import socket
import threading

# Configuração do servidor
HOST = "127.0.0.1"  # IP local
PORT = 5000         # Porta para comunicação

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []  # Lista para armazenar conexões ativas

def broadcast(message, client_socket):
    """ Envia a mensagem para todos os clientes conectados, menos para quem enviou """
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                clients.remove(client)

def handle_client(client):
    """ Gerencia mensagens de um cliente """
    while True:
        try:
            message = client.recv(1024)
            if not message:
                break
            broadcast(message, client)
        except:
            clients.remove(client)
            break

    client.close()

def start_server():
    print(f"Servidor rodando em {HOST}:{PORT}")
    while True:
        client, address = server.accept()
        print(f"Nova conexão: {address}")
        clients.append(client)

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

start_server()