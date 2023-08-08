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

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 8080))

root = Tk()
root.title("Collaborative Canvas")
canvas = Canvas(root, width=800, height=600, bg="white")
