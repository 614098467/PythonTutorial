
import threading  # 线程
import time


def HelloWorld(num):
    time.sleep(3)
    print("Hello %s" %num)




if __name__ == "__main__":
    HelloWorld(3)

    T1 = threading.Thread(target=HelloWorld,args=(22,))
    T1.start()

    T2 = threading.Thread(target=HelloWorld,args=(11,))
    T2.start()

    print("ending.....")


