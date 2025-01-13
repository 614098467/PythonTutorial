import queue


# q = queue.Queue()  # FIFO

# q.put(2)
# q.put("hello")
# q.put({"name":"张三"})

# while 1:
#     data = q.get()
#     print(data)


# q = queue.LifoQueue() 
#  # LIFO

# q.put(2)
# q.put("hello")
# q.put({"name":"张三"})

# while 1:
#     data = q.get()
#     print(data)

q = queue.PriorityQueue()

q.put([2,12])
q.put([4,'hello'])
q.put([5,{"hello":"world"}])

while 1 :
    data = q.get(block=False)
    print(data)
