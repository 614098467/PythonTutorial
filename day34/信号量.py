import threading,time

class Mythread(threading.Thread):
    def run(self):
        if semaphore.acquire():
            print(self.name)
            time.sleep(3)
            semaphore.release()


if __name__ == "__main__":
    semaphore = threading.Semaphore(5)

    threading_list = []
    for i in range(20):
        threading_list.append(Mythread())
    for t in threading_list:
        t.start()
    
    for t in threading_list:
        t.join()
    
    print("end-----")




