from django.shortcuts import render,HttpResponse

import time
# Create your views here.


def show_time(req):
    cur_time = time.ctime()

    return render(req,"index.html",{"time":cur_time})


def article_year(req,year):
    return HttpResponse("year: %s"%year)


def article_year_month(req,year,month):
    return HttpResponse("year: %s ,month %s" %(year,month))


def register(req):

    if req.method == "POST":
        print(req.POST.get('user'))
        print(req.POST.get('age'))
        return HttpResponse("SUCCESS!!")
    if req.method == "GET":
        print(req.GET.get('user'))
        print(req.GET.get('age'))
    return render(req,"register.html")



