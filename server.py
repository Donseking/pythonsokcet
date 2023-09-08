import socket, threading

HOST = "192.168.50.222"
POST = 4717

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, POST))
server.listen()

clients = []
nicknames = []

def broadcast(msg) :
    for c in clients :
        c.send(msg)

def handle(c) :
    while True :
        try :
            msg = c.recv(1024)
            broadcast(msg)
        except :
            index = clients.index(c)
            clients.remove(c)
            c.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} 離開了 !!".encode("UTF8"))
            nicknames.remove(nickname)
            break

def receive() :
    while True :
        c, addr = server.accept()
        print(f"FROM : \n   > {str(addr)}")

        c.send("nick".encode("UTF8"))
        nickname = c.recv(1024).decode("UTF8")
        nicknames.append(nickname)
        clients.append(c)
        print(f"{nickname}已連接")
        broadcast(f"{nickname}已加入聊天室".encode("UTF8"))
        c.send("已連接".encode("UTF8"))

        thread = threading.Thread(target = handle, args = (c, ))
        thread.start()

receive()