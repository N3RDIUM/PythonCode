import socket
import threading
import json

from config import ADDRESS, PORT

client_threads = []
clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ADDRESS, PORT))
server.listen(1024)

print(f"Server is listening on {ADDRESS}:{PORT}")

def handle_client(conn, addr):
    print(f"New connection from {addr[0]}:{addr[1]}")
    uname = None
    other_uname = None
    while True:
        data = conn.recv(1024)
        if not data or data == b"":
            conn.close()
        else:
            data = json.loads(data.decode())
            if 'username' in data.keys():
                uname = data['username']
            if 'other_username' in data.keys():
                other_uname = data['other_username']
        if uname is not None and other_uname is not None:
            break
    clients.append({
        "conn": conn,
        "uname": uname,
        "other_uname": other_uname
    })
    print(f"Got client details: {str(clients[-1])}")
    
    while True:
        data = conn.recv(1024)
        if not data or data == b"": continue
        data = json.loads(data.decode())
        if data['type'] == "message":
            for client in clients:
                if client['uname'] == data['other_username']:
                    print(f"Sending message to {client['uname']}")
                    client['conn'].send(json.dumps({
                        "type": "message",
                        "message": data['message']
                    }).encode())
    
while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
    client_threads.append(thread)