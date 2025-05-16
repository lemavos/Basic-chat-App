# Basic Chat App

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is a basic chat application written in Python using sockets. It allows multiple clients to connect to a server and exchange messages in real-time. The server listens for connections, and each client can send messages that will be broadcast to all connected clients.

## 🚀 Features

- Real-time communication between clients
- Multi-client support
- Simple and minimalistic terminal interface
- Educational example for learning sockets in Python

## 🧑‍💻 Technologies Used

- `socket`
- `threading`

## 📋 How to Run

### 🐧 On Linux / 🪟 On Windows:

1. Make sure you have Python 3 installed.
   ```bash
   python3 --version
   ```

2. Clone the repository:
   ```bash
   git clone https://github.com/Henriquelemos911/Basic-chat-App.git
   cd Basic-chat-App
   ```

3. Run the server:
   ```bash
   cd server
   python3 server.py
   ```

4. In another terminal, run one or more clients:
   ```bash
   cd client
   python3 client.py
   ```

5. Enter your name when prompted and start chatting!

## 🤖 How It Works

- The server creates a socket and listens on port `55555` for incoming connections.
- Each client connects to the server and starts a new thread to handle sending and receiving messages.
- Messages sent by any client are broadcast to all connected clients.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
