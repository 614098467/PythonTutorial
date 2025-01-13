import time,random
import queue,threading


q = queue.Queue()

def Producer(name):
    count = 0
    while count < 10:
        print("making food")
        time.sleep(random.randrange(2))
        q.put(count)
        print(" %s has made %s food" %(name,count))
        count += 1
        # q.task_done()   ## 告诉队列已经完成了动作
        q.join()   ## 收到队列完成了
        print("OK!")

def Customer(name):
    count =  0
    while count < 10:
        time.sleep(random.randrange(4))
        if not q.empty():
            data = q.get()
            # q.join()   ## 收到队列完成了
            q.task_done()
            print(" %s has eat %s food" %(name,data))
        else:
            print("no food")
        count += 1



p1 = threading.Thread(target=Producer,args=("Producer1",))
c1 = threading.Thread(target=Customer,args=("Customer1",))
c2 = threading.Thread(target=Customer,args=("Customer2",))
c3 = threading.Thread(target=Customer,args=("Customer3",))

p1.start()
c1.start()
c2.start()
c3.start()

p1.join()
c1.join()
c2.join()
c3.join()

print("end----")

