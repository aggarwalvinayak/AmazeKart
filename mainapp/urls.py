from django.urls import path

# from .views import  UserList,ProductList,ImageList
from .views import ProductList,LoginApi,RegisterApi,Form,Upload
from . import views


app_name = "mainapp"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
	# path('userdatabase/',  UserList.as_view()),
	path('productdatabase/',  ProductList.as_view()),
	path('loginapi/',  LoginApi.as_view()),
	path('registerapi/',RegisterApi.as_view()),
	path('store/',  views.store, name="store"),
	# path('image/', views.DocumentCreate, name = 'hotel_images'),
	path('form/', views.Form),
	path('upload/', views.Upload),

]
