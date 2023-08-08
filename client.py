import socket
import threading
from tkinter import *

def send_data(event):
    data = canvas.create_text(event.x, event.y, text="*", fill="red")
    data = f"{event.x},{event.y}\n"
    client_socket.sendall(data.encode())

def receive_data():
    while True:
        data = client_socket.recv(1024).decode()
        coords = data.split(',')
        x, y = int(coords[0]), int(coords[1])
        canvas.create_text(x, y, text="*", fill="blue")
