import socket
import threading
from tkinter import *

def send_data(event):
    data = canvas.create_text(event.x, event.y, text="*", fill="red")
    data = f"{event.x},{event.y}\n"
    client_socket.sendall(data.encode())

def receive_data():
