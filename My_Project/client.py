import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 1255
s.connect((host,port))
con = True
while con:
    msg = input("enter msg : ")
    s.send(msg.encode("utf-8"))
    if msg == "quit":
        con = False
        s.close()
