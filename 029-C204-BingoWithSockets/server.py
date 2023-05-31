import time
import socket
import random
import settings as config

# Start the server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((config.ADDRESS, config.PORT))
sock.listen(config.MAX_PLAYERS)
announced = []

# Create a list of players
players = []
while True:
    conn, addr = sock.accept()
    conn.settimeout(1/20)
    print(f"New connection from {addr}")
    username = conn.recv(1024).decode('utf-8')
    players.append((username, conn))
    print(f"Added {username} to the list of players")
    if len(players) == config.MIN_PLAYERS:
        break

print("Starting game...")

gover = False
while True and not gover:
    num = str(random.randrange(config.RANDOM_RANGE[0], config.RANDOM_RANGE[1]))
    while num in announced:
        num = str(random.randrange(config.RANDOM_RANGE[0], config.RANDOM_RANGE[1]))
    announced.append(num)
    print(f"Announcing {num}")
    for player in players:
        conn = player[1]
        conn.send(num.encode('utf-8'))
        try:
            dat = conn.recv(1024)
            if dat is not None:
                if dat.decode('utf-8') == "i win":
                    for player in players:
                        conn = player[1]
                        conn.send(f"game over, {player[0]} won".encode('utf-8'))
                    gover = True
        except TimeoutError:
            pass
    time.sleep(1)
