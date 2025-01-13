

def Plus(num):
    total = 0
    for i in range(1,num+1):
        total += i
    print(total)
    return total

def Mul(num):
    total = 1
    for i in range(1,num+1):
        total *= i
    print(total)
    return total

import threading
import time 

start = time.time()

t1 = threading.Thread(target=Plus,args=(10000,))
t2 = threading.Thread(target=Mul,args=(10,))

l = []

l.append(t1)
l.append(t2)

for i in l:
    i.start()

for i in l:
    i.join()

end = time.time()
cost_time = end - start
print("%s"%cost_time)

