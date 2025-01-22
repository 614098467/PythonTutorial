from django.shortcuts import render,HttpResponse,redirect
import time
import django
# Create your views here.

def show_time(req):
    # t = time.ctime()
    t = [1,2,3]
    name = 'yuan'
    d = {'name':'alex','age':12,'hobby':'baskerball'}

    test = 10

    return render(req,'show_time.html',locals())


def register(req):
    print(req.path)

    if req.method == 'POST':
        print(req.POST.get('user'))
        print(req.POST.get('age'))
        user = req.POST.get('user')
        if user == 'zg':
            return redirect('login')
        return HttpResponse("SUCCESS!!")

    # return render(req,'1.html')

    return render(req,'1.html')


def login(req):
    name = 'zg'

    return render(req,'login.html',{'name':name})

    
def backend(req):
    
    return render(req,'base.html')

def student(req):

    std_list = ['alex','bob','cici']
    return render(req,'student2.html',locals())

def teacher(req):

    return render(req,'teacher.html')

def class_(req):

    return render(req,'class.html')
