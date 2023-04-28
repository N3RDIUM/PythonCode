# Socket chatroom client
import socket
import threading
import time

# Get the IP address of the server from the user
SERVER = input("Enter server IP: ")
PORT = 9999
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
USERNAME = input("Enter username: ")

# Create a new socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the server
client.connect(ADDR)

# Send the username to the server
client.send(USERNAME.encode(FORMAT))

def receive():
    connected = True
    while connected:
        # Wait for a message from the server
        msg_length = client.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = client.recv(msg_length).decode(FORMAT)
            
            if msg == DISCONNECT_MESSAGE:
                connected = False
            
            print(f"[SERVER] {msg}")

def send():
    connected = True
    while connected:
        # Wait for the user to input a message
        msg = input()
        # Send message length to the server
        client.send(str(len(msg)).encode(FORMAT))
        time.sleep(0.1)
        # Send the message to the server
        client.send(msg.encode(FORMAT))
        
        if msg == DISCONNECT_MESSAGE:
            connected = False
            
if __name__ == "__main__":
    while True:
        receive_thread = threading.Thread(target=receive)
        receive_thread.start()
        send()