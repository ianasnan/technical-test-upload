from django.urls import path
from . import views

app_name = 'sdm'
urlpatterns = [
    path("login/", views.login_user, name="login"),
    path("proseslogin/", views.proses_login, name="proseslogin"),
    path("register/", views.register_user, name="register_user"),
    path("logout_user/", views.logout_user, name="logout_user"),
    path("home/", views.home , name="home"),
    path("upload/", views.uploadData , name="uploadData"),
    path("dataImage/", views.dataImage , name="dataImage"),
    path("detailImage/", views.detailImage , name="detailImage"),
]
