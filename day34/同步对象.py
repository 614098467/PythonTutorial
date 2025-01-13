
import threading,time

class Boss(threading.Thread):
    def run(self):
        print("Boss:加班")
        print(event.is_set())
        event.set()
        time.sleep(5)
        print("Boss:下班")
        print(event.is_set())
        event.set()

class Worker(threading.Thread):
    def run(self):
        event.wait() # 一旦event被设定，等同于pass
        print("Worker:开始工作\n")
        time.sleep(1)
        event.clear()
        event.wait()
        print("Worker:结束工作")


if __name__ == "__main__":
    event = threading.Event()
    list_thread = []
    for i in range(5):
        t = Worker()
        list_thread.append(t)
    list_thread.append(Boss())
    for t in list_thread:
        t.start()
    for t in list_thread:
        t.join()
    print("end")