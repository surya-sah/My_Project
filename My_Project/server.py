import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
# host = "192.168.1.110"
port = 1255
s.bind((host,port))
s.listen(5)
socketclient, address = s.accept()
print("got connection formed", address)
con = True
while con:
    msg = socketclient.recv(1024)    #size of buffer
    msg = msg.decode("utf-8")
    print(msg)
    if (msg=="quit"):
        con = False
        s.close()
        