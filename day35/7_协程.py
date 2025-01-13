## 生成器


def f():
    print("ok")
    yield

    ## 调用next相当于从当前出去，再调用相当于再回来再进行下边的代码
    print("ok2")
    yield



# g = f()
# g1 = g.__next__()
# print(g1)
# print(next(g))



def f2():
    print("ok")
    num = yield
    print("num",num)
    yield

g = f2()
g1 = g.__next__()
g.send(5)
