from django.urls import path

# from .views import  UserList,ProductList,ImageList
from .views import register,login_request,logout_request


app_name = "customuser"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login_request, name="login"),
    path("logout/", logout_request, name="logout"),

]