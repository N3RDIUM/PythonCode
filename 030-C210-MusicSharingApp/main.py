import tkinter

class MusicSharingApp:
    def __init__(self):
        self.root = tkinter.Tk()
        self.uname = "User1"
        self.other_uname = "User2"
        
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
        self.message_list = []
        self.messages = tkinter.Listbox(self.root, width=100, height=20, bg="white", fg="black")
        self.messages.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
        
        self.scrollbar = tkinter.Scrollbar(self.root)
        self.scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        
        self.messages.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.messages.yview)
        
        self.inputtext = tkinter.Label(self.root, text="Message:")
        self.inputtext.pack(side=tkinter.LEFT)
        
        self.input = tkinter.Entry(self.root, width=40)
        self.input.pack(side=tkinter.RIGHT)
        
        self.send = tkinter.Button(self.root, text="Send", command=self.send_message)
        self.send.pack(side=tkinter.BOTTOM)
        
        self.file = tkinter.Button(self.root, text="Attach", command=self.send_file)
        self.file.pack(side=tkinter.BOTTOM)
    
    def send_message(self):
        message = self.input.get()
        self.message_list.append(message)
        self.messages.insert(tkinter.END, message)
        self.input.delete(0, tkinter.END)
    
    def send_file(self):
        print("Sending file...")
    
    def main(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = MusicSharingApp()
    app.main()