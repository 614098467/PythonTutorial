
from wsgiref.simple_server import make_server

import time


def FOO(req):
    f = open('index1.html','rb')
    data = f.read()
    return data

def login(req):

    return b'welcome!'
    pass

def signup(req):
    pass


def showtime(req):
    cur_time = time.ctime()
    # return ('<h1> time: %s </h1>' %str(cur_time)).encode('utf8')
    # f = open('1_showtime.html','rb')
    # data = f.read()
    # data.decode('utf8').replace('@time@',cur_time)
    # return data.encode('utf8')
    with open('1_showtime.html','rb') as f:
        data = f.read()
    modified_data = data.decode('utf8').replace('@time@',cur_time)
    return modified_data.encode('utf8')
    


def router():
    url_patterns = [
        ('/login',login),
        ('/signup',signup),
        ('/showtime',showtime)
    ]
    return url_patterns


def application(environ,start_response):

    start_response('200 OK',[('Content-Type','text/html')])
    path = environ['PATH_INFO']

    url_patterns = router()

    func = None
    for item in url_patterns:
        if item[0] == path:
            func = item[1]
            break
    if func:
        return [func(environ)]
    else:
        return [b'<h1>404</h1>']




httpd = make_server('',8080,application)
print("Serving HTTP on port 8080")
# 开始监听HTTP请求
httpd.serve_forever()


