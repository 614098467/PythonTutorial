from greenlet import greenlet
'''greenlet 实现协程的切换操作'''


def test1():
    print(56)
    grl2.switch()
    print(57)


def test2():
    print(68)
    grl.switch()
    print(99)

grl = greenlet(test1)
grl2 = greenlet(test2)

grl.switch()