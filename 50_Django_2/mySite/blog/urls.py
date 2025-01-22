
from django.contrib import admin
from django.urls import path,re_path,include
from blog import views


urlpatterns = [
    path(r'register',views.register,name='reg'),
    path(r'login',views.login,name = 'login'),
    
]
