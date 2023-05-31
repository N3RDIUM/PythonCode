import random
import threading
import settings as config

card = []
for i in range(random.randrange(config.RANDOM_CARD_RANGE[0], config.RANDOM_CARD_RANGE[1])):
    card.append(random.randrange(config.RANDOM_RANGE[0], config.RANDOM_RANGE[1]))

import tkinter as Tk
from tkinter import simpledialog as sd
import socket

if __name__ == "__main__":
    while True:
        # Get the username from the user
        username = str(sd.askstring("Username", "What is your username?"))
        if username is not None:
            break

    # First connect to the server
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((config.ADDRESS, config.PORT))
    sock.send(username.encode('utf-8'))

    # Now, we can create our GUI window
    window = Tk.Tk()
    window.title("Bingo")
    window.config(bg="black")
    window.geometry("700x900") # widescreen
    window.resizable(False, False)

    # Add the widgets to the window
    title = Tk.Label(window, text=f"Bingo: {username}", font=("Arial", 50), bg="black", fg="white")
    title.pack()
    
    # Add the card to the window
    quads = []
    labels = []
    labelnums = []
    idx = 0
    while not idx == len(card) - 1:
        quad = Tk.Frame(window, bg="black")
        quad.pack()
        for i in range(5):
            if idx == len(card) - 1:
                break
            if random.choice([True,True,True,False]):
                label = Tk.Label(quad, text=card[idx], font=("Arial", 50), bg="black", fg="white")
                label.pack(side=Tk.LEFT)
                labels.append(label)
                idx += 1
                labelnums.append(card[idx])
            else:
                label = Tk.Label(quad, text="__", font=("Arial", 50), bg="black", fg="black")
                label.pack(side=Tk.LEFT)
            label = Tk.Label(quad, text="__", font=("Arial", 50), bg="black", fg="black")
            label.pack(side=Tk.LEFT)
        quads.append(quad)
        
    # Add the announcer to the window
    announcer = Tk.Label(window, text="Waiting for announcer...", font=("Arial", 50), bg="black", fg="white")
    announcer.pack()
    
    # Start listening for numbers
    def _():
        global sock
        global announcer
        global labels
        while True:
            num = sock.recv(1024).decode('utf-8')
            announcer.config(text=f"Announcer: {num}")
            try:
                for label in labels:
                    if int(label.cget("text")) == int(num):
                        label.config(fg="green")
                _ = False
                for label in labels:
                    if not label.cget("fg") == "green":
                        _ = True
                if not _:
                    sock.send("i win".encode('utf-8'))
                    break
            except:
                break
    thread = threading.Thread(target=_, daemon=True)
    thread.start()
    # Run mainloop
    window.mainloop()
