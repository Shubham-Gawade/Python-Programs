import socket

ss = socket.socket()
#By default -> IPv4 and TCP

print('Socket Created')

ss.bind(("localhost",9999))  #port no range -> 0 to 65535

ss.listen(3)  # how many client connection

print("Waiting for connections...")

while True:
    cs,address=ss.accept()
    name = cs.recv(1024).decode()
    print("Connected with",address," ",name)

    cs.send(bytes("Welcome shubham","utf-8"))

    cs.close()


