import socket, threading

HOST = "192.168.50.222"
POST = 4717

nickname = input("請輸入暱稱\n    > ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, POST))


def receive() :
    while True :
        try :
            msg = client.recv(1024).decode("UTF8")
            if msg == "nick" :
                client.send(nickname.encode("UTF8"))
            else :
                print(msg)
        except :
            print("Client.py > [19] : Error")
            client.close()
            break

def write() :
    while True :
        msg = f"{nickname} : {input('')}"
        client.send(msg.encode("UTF8"))

receive_threading = threading.Thread(target = receive)
receive_threading.start()

write_threading = threading.Thread(target = write)
write_threading.start()