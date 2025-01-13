from multiprocessing import Pool,Process
import time,os

def Foo(i):
    time.sleep(1)
    print(i)
    return i+100


def Bar(arg):
    print(os.getpid())
    print(os.getppid())

    print("logger",arg)


if __name__ == '__main__':
    pool = Pool()

    # Bar(1)
    print("----------------------")
    for i in range(10):
        # pool.apply(func=Foo,args=(1,))
        # pool.apply_async(func=Foo,args=(i,))

        ## call_back：某个函数执行成功后再去执行的函数，
        pool.apply_async(func=Foo,args=(i,),callback=Bar)


    ## 进程池的格式 就是close后边加上join

    pool.close()
    pool.join()