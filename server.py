import socket
import threading

clients = []
canvas = []

def handle_client(client_socket):
    global canvas
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            canvas.append(data)
            for client in clients:
                client.sendall(data.encode())
        except:
            break

    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
