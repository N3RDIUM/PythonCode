# Socket chatroom server
import socket
import threading
import time
from config import PORT
import fuzzywuzzy.fuzz
import json

# Choose a port that is free
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

# Create a new socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the address
server.bind(ADDR)

connections = []

# Load the quiz questions
with open("quiz_questions.json", "r") as f:
    quiz = json.load(f)
    quiz = [[question, answer] for question, answer in quiz.items()]
print(quiz)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    
    connected = True
    username = conn.recv(HEADER).decode(FORMAT)
    _ = f"Welcome to the quiz, {username}!".encode(FORMAT)
    conn.send(str(len(_)).encode(FORMAT))
    time.sleep(0.1)
    conn.send(_)
    nextq = True
    currq = -1
    while connected:
        if nextq:
            print("Sending next question")
            currq += 1
            if currq >= len(quiz):
                for connection in connections:
                    connection.send(str(len("Quiz finished! Well done!")).encode(FORMAT))
                    time.sleep(0.1)
                    connection.send("Quiz finished! Well done!".encode(FORMAT))
            else:
                for connection in connections:
                    connection.send(str(len("Question:")).encode(FORMAT))
                    time.sleep(0.1)
                    connection.send("Question:".encode(FORMAT))
                    time.sleep(0.1)
                    connection.send(str(len(quiz[currq][0])).encode(FORMAT))
                    time.sleep(0.1)
                    connection.send(quiz[currq][0].encode(FORMAT))
            nextq = False
        # Wait for a message from the client
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            
            if msg == DISCONNECT_MESSAGE:
                connected = False
            
            print(f"[{addr}] {msg}")
            
            ratio = fuzzywuzzy.fuzz.ratio(msg, quiz[currq][1])
            if ratio >= 90:
                msg = f"[{username}] got the correct answer: {msg}"
                nextq = True
            else:
                msg = f"[{username}] better luck next time!"
                nextq = False
            
            for connection in connections:
                # Send the message length to the clients
                connection.send(str(len(msg)).encode(FORMAT))
                time.sleep(0.1)
                # Send the message to the client
                connection.send(msg.encode(FORMAT))
    conn.close()
    
def start():
    # Listen for connections
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    
    while True:
        # Wait for a new connection
        conn, addr = server.accept()
        connections.append(conn)
        
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
        
if __name__ == "__main__":
    print("[STARTING] Server is starting...")
    start()