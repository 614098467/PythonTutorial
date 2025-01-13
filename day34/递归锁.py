
import threading
import time
class Mythtread(threading.Thread):

    def actionA(self):
        r_lock.acquire()
        print(self.name,"got lock A",time.ctime())
        time.sleep(2)
        
        r_lock.acquire()
        print(self.name,"got lock B",time.ctime())
        time.sleep(1)
        
        r_lock.release()
        r_lock.release()

    def actionB(self):
        r_lock.acquire()
        print(self.name,"got lock B",time.ctime())
        time.sleep(2)
        
        r_lock.acquire()
        print(self.name,"got lock A",time.ctime())
        time.sleep(1)

        r_lock.release()
        r_lock.release()

    def run(self):
        self.actionA()
        self.actionB()

 


if __name__ == "__main__":
    # A = threading.Lock()
    # B = threading.Lock()

    r_lock = threading.RLock()
    list_thread = []
    for i in range(5):
        t = Mythtread()
        t.start()
        list_thread.append(t)

    for t in list_thread:
        t.join()

    print("end")