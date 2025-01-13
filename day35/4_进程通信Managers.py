
from multiprocessing import Manager,Process


def f(d,l,n):
    d[n] = '1'
    d['2'] = 2

    l.append(n)

    print("son process",id(d),id(l))




if __name__ == "__main__":
    

    with Manager() as manager:
        d = manager.dict()
        li = manager.list()

        print("father process:",id(d),id(li))
        P_list = []
        for i in range(10):
            P = Process(target=f,args=(d,li,i))
            P_list.append(P)
        for p in P_list:
            p.start()
            p.join()

        print(d,li)
        
        print("end !!!!")
        
            
    

