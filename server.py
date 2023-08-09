import socket
import threading

clients = []
canvas = []

def handle_client(client_socket):
    global canvas
    while True:
        try:
