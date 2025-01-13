

import os
import time
from multiprocessing import Process
def info(title):
    print("title:",title)
    print("parent process:",os.getppid())
    print("process id:",os.getpid())
    print("--------------------------------")

def f(name):
    info("function f")
    print("hello",name)

if __name__ == "__main__":
    info("main line")
    time.sleep(1)
    p = Process(target=f,args=("bob",))
    p2 = Process(target=f,args=("bob2",))
    p.start()
    p2.start()
    p.join()
    p2.join()