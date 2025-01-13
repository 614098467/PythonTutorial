import threading
import time 

def music():
    print("begin to listen %s" %time.ctime())
    time.sleep(3)
    print("end to listen %s" %time.ctime())

def movie():
    print("begin to watch %s" %time.ctime())
    time.sleep(5)
    print("end to watch %s" %time.ctime())



if __name__ == "__main__":
    # fun_name = ["music","movie"]
    # for i in range(2):
    #     exec(f"t{i} = threading.Thread(target={fun_name[i]})")
    #     exec(f"t{i}.start()")
    # print("ending....")

    # t1 = threading.Thread(target=music)
    # t2 = threading.Thread(target=movie)
    # t1.start()
    # t1.join()
    # t2.start()
    # # t1.join() # t1线程执行完毕后，再执行主线程
    # # t2.join()  # t2线程执行完毕后，再执行主线程
    # print("ending....")

    t1 = threading.Thread(target=music)
    t2 = threading.Thread(target=movie)
    threading = []
    threading.append(t1)
    threading.append(t2)
    t2.setDaemon(True)
    for t in threading:
        t.start()


    print("ending....")


