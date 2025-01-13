
import time
import threading

l = threading.Lock()
def sub():
    global num
    l.acquire()
    temp = num
    time.sleep(0.0001)
    num = temp - 1
    l.release()



num = 100



import threading

list_thread = []

for i in range(100):
    t = threading.Thread(target=sub)
    t.start()
    list_thread.append(t)

for t in list_thread :
    t.join()


print(num)
