# Socket chatroom client
import socket
import threading
import time
import tkinter as tk
from tkinter import simpledialog as sd
from config import PORT

# Get the IP address of the server from the user
SERVER = "127.0.1.1"
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

class ChatWindow():
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(ADDR)
        
        self.receive_thread = threading.Thread(target=self.receive)
        self.receive_thread.start()
        
        self.username = str(sd.askstring("Username", "What is your username?"))
        self.client.send(self.username.encode(FORMAT))
        print(f"User registered as {self.username}")
        
        self.window = tk.Tk()
        self.window.deiconify()
        self.window.title("CHATROOM")
        self.window.resizable(width=False, height=False)
        
        # Create the chat GUI now that we have a username
        # Create a input box and bind the enter key to send
        self.terminal = tk.Text(self.window, width=160, height=30, fg="white", bg="black")
        self.terminal.pack(side="top")

        self.textbox = tk.Entry(self.window, width=160, fg="white", bg="black")
        self.textbox.pack(side="bottom")
        self.textbox.bind("<Return>", self.send_message)
        
        self.window.mainloop()
    
    def send_message(self, *args, **kwargs):
        print(f"Do something with this to prevent bugs: {args} {kwargs}")
        self.send(self.textbox.get())
        # Clear the textbox
        self.textbox.delete(0, tk.END)
        
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
                self.terminal.insert(tk.END, f"{msg}\n")

    def send(self, msg):
        # Send message length to the server
        self.client.send(str(len(msg)).encode(FORMAT))
        time.sleep(0.1)
        # Send the message to the server
        self.client.send(msg.encode(FORMAT))
            
if __name__ == "__main__":
    win = ChatWindow()
    win.connected = False