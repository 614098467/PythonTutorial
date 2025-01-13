
from multiprocessing import Process,Lock


def f(l,i):
    with l:
        print("hello world %s"%i)


if __name__ == "__main__":
    lock = Lock()

    for num in range(10):
        p = Process(target=f,args=(lock,num))
        p.start()
        p.join()

