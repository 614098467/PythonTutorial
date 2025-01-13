import gevent
import requests,time

'''gevent 实现协程的自动IO切换'''

start = time.time()

def f(url):
    print("Get : %s" %url)
    resp = requests.get(url=url)
    data = resp.text
    print("%d bytes received from %s" %(len(data),url))


gevent.joinall([
    gevent.spawn(f,'https://www.python.org'),
    gevent.spawn(f,'https://www.baidu.com'),
    gevent.spawn(f,'https://www.hao123.com'),
])

end_time = time.time()

print("time: %s" %(start - end_time))