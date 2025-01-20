


from django.urls import path,re_path
from blog import views


urlpatterns = [

    path(r"register",views.register,name="reg"),
    # path(r"article/2004",views.article_year)
    # path(r'^article/(\d{4})',views.article_year)
    re_path(r"^article/(\d{4})$", views.article_year),

    re_path(r"^article/(?P<year>\d{4})/(?P<month>\d{2})",views.article_year_month),

]

