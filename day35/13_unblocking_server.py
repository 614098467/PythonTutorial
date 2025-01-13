import socket
import time
sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 设置socket选项 SO_REUSEADDR 为1,允许在同一端口上重复启动服务器
# 这样可以避免服务器重启时提示"地址已被使用"的错误
# 当服务器意外关闭后,端口会处于TIME_WAIT状态,没有这个设置的话需要等待一段时间才能重新绑定该端口
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sk.bind(("127.0.0.1",6667))

sk.listen(5)

sk.setblocking(False)

print("waiting client response")
while True:
    try:
        connection,address = sk.accept()
        print("++++",address)
        client_message = connection.recv(1024)
        print(str(client_message,"utf8"))
        connection.close()
    except Exception as e:
        print(e)
        time.sleep(3)



