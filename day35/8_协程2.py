import time
import queue
'''yield 来实现协程的切换操作'''


def consumer(name):
    print("---> ready to eat baozi")
    while True:
        new_baozi = yield
        print("[%s] is eating baozi %s" %(name,new_baozi))


def producer():
    r = con.__next__()
    r = con2.__next__()
    n = 0
    while 1:
        time.sleep(1)
        print("\033[321m[producer]\033[0m is making baozi %s and %s]" %(n,n+1))
        con.send(n)
        con2.send(n+1)

        n+=2


if __name__ == '__main__':
    con = consumer("c1")
    con2 = consumer("c2")
    p = producer()