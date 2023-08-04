import json
import socket
import tkinter
from tkinter.simpledialog import askstring

from config import ADDRESS, PORT

class MusicSharingApp:
    def __init__(self):
        self.uname = askstring("Username", "Enter your username:")
        self.other_uname = askstring("Username", "Enter the username of the person you want to chat with:")
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((ADDRESS, PORT))
        
        self.root = tkinter.Tk()
        self.root.title(f"{self.uname}->{self.other_uname}: Music Sharing App")
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        
        # Create the widgets
        #  _________________
        # |                 |
        # | [messages]      |
        # |                 |
        # |                 |
        # |                 |
        # | [in, snd, file] |
        # |_________________|
        self.messages = tkinter.Listbox(self.root, width=100, height=20, bg="white", fg="black")
        self.messages.pack(expand=False)
        
        self.inputtext = tkinter.Label(self.root, text="Message:")
        self.inputtext.pack(side=tkinter.LEFT)
        
        self.input = tkinter.Entry(self.root, width=40)
        self.input.pack(side=tkinter.LEFT)
        
        self.send = tkinter.Button(self.root, text="Send", command=self.send_message)
        self.send.pack(side=tkinter.LEFT)
        
        self.file = tkinter.Button(self.root, text="Attach", command=self.send_file)
        self.file.pack(side=tkinter.LEFT)
    
    def send_message(self):
        message = self.input.get()
        self.messages.insert(tkinter.END, message)
        self.input.delete(0, tkinter.END)
        self.sock.send(json.dumps({
            'type': 'message',
            'message': message,
        }).encode())
        
    def recv_messages(self):
        rcvd = self.sock.recv(1024)
        if not rcvd or rcvd == b"": return
        rcvd = json.loads(rcvd.decode())
        if rcvd['type'] == "message":
            self.messages.insert(tkinter.END, rcvd['message'])
    
    def send_file(self):
        # Code to attach a file goes here
        pass
    
    def main(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = MusicSharingApp()
    app.main()