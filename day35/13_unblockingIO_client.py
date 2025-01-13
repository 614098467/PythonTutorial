import socket
sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


sk.connect(("127.0.0.1",6667))

sk.send("hello".encode("utf-8"))
    