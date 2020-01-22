from django.urls import path

# from .views import  UserList,ProductList,ImageList
from .views import ProductList,ImageList
from . import views


app_name = "mainapp"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    # path('userdatabase/',  UserList.as_view()),
    path('productdatabase/',  ProductList.as_view()),
    path('imagedatabase/',  ImageList.as_view()),
    path('store/',  views.store, name="store"),

]