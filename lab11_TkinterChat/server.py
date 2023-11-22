import socket
import threading

clients = {}

def broadcast(message, sender_name):
    for client_socket, (name_socket, name) in clients.items():
        try:
            client_socket.send(f"{sender_name}: {message}".encode())
        except socket.error:
            pass

def handle_client(client_socket, client_address):
    client_socket.send("Welcome to the chat! Enter your name: ".encode())
    name = client_socket.recv(1024).decode()

    clients[client_socket] = (client_socket, name)
    print(f"Client {name} connected from {client_address}")

    try:
        while True:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(f"Received from {name}: {message}")
            broadcast(message, name)
    except socket.error:
        pass

    del clients[client_socket]
    print(f"Client {name} disconnected.")
    client_socket.close()


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen()

    print("Server listening on port 12345...")

    while True:
        client_socket, client_address = server.accept()
        client_handler = threading.Thread(
            target=handle_client, args=(client_socket, client_address)
        )
        client_handler.start()

if __name__ == "__main__":
    start_server()
