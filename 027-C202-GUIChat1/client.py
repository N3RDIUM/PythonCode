# Socket chatroom client
import socket
import threading
import time
import tkinter as tk
from tkinter import simpledialog as sd

# Get the IP address of the server from the user
SERVER = "127.0.1.1"
PORT = 9999
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

class ChatWindow(tk.Frame):
    def __init__(self):
        super(ChatWindow, self).__init__(height=400, width=600)
        
        # Create a new socket
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(ADDR)
        
        self.receive_thread = threading.Thread(target=self.receive)
        self.receive_thread.start()

        self.new_messages = []
        
        # FIXME: We need to send the username to the server: self.client.send(USERNAME.encode(FORMAT))
        # Create an input dialog box to get the username from the user
        self.username = str(sd.askstring("Username", "What is your username?"))
        self.client.send(self.username.encode(FORMAT))
        print(f"User registered as {self.username}")
        
    def receive(self):
        self.connected = True
        while self.connected:
            # Wait for a message from the server
            msg_length = self.client.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = self.client.recv(msg_length).decode(FORMAT)
                
                if msg == DISCONNECT_MESSAGE:
                    self.connected = False
                
                print(f"[SERVER] {msg}")
                self.new_messages.append(msg)

    def send(self, msg):
        # Send message length to the server
        self.client.send(str(len(msg)).encode(FORMAT))
        time.sleep(0.1)
        # Send the message to the server
        self.client.send(msg.encode(FORMAT))
            
if __name__ == "__main__":
    win = ChatWindow()
    win.mainloop()
    win.connected = False