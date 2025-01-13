from multiprocessing import Process
import multiprocessing
import queue
import time



'''放任务'''
def put_task(q):
    q.put(2)
    q.put("Hello!")


def get_task():
    time.sleep(2)
    if q.empty():
        print("任务队列为空")
    else:
        print(q.get())


if __name__ == "__main__":
    q = multiprocessing.Queue()
    P1 = Process(target=put_task,args=(q,))
    P1.start()
    P1.join()

    get_task()


    print("主进程执行结束")