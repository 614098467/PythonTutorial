
from multiprocessing import Pipe,Process

def f(conn):
    conn.send(["hello",{"name":"张三"},111])
    response = conn.recv()
    print("response:",response)
    conn.close()
    print("q_id2",id(conn))


if __name__ == "__main__":
    parent_conn,child_conn = Pipe()       ## 双向管道
    print("q_id1",id(parent_conn)) 
    p = Process(target=f,args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    parent_conn.send("hello")
    p.join()
    print("主进程执行结束")