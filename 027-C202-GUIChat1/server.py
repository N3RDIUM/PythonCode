# Socket chatroom server
import socket
import threading
import time

# Choose a port that is free
PORT = 9999
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

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    
    connected = True
    username = conn.recv(HEADER).decode(FORMAT)
    _ = f"Welcome to the chatroom, {username}! Type !DISCONNECT to leave.".encode(FORMAT)
    conn.send(str(len(_)).encode(FORMAT))
    time.sleep(0.1)
    conn.send(_)
    while connected:
        # Wait for a message from the client
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            
            if msg == DISCONNECT_MESSAGE:
                connected = False
            
            print(f"[{addr}] {msg}")
            
            msg = f"[{username}] {msg}"
            
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