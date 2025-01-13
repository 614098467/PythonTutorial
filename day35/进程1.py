import time
from multiprocessing import Process

class MyProcess(Process):
    def __init__(self,num):
        super(MyProcess,self).__init__()
        self.num = num

    def run(self):
        time.sleep(1)
        print(self.pid)
        print(self.is_alive())
        print(self.num)
        time.sleep(1)

    


if __name__ == "__main__":
    Process_list = []

    for i in range(10):
        p = MyProcess(i)
        Process_list.append(p)
    for p in Process_list:
        p.start()
        p.join()
    print("主进程执行结束")