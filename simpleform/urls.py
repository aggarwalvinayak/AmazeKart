from django.urls import path

from .views import  UserDatabaseList


app_name = "simpleform"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('userdatabase/',  UserDatabaseList.as_view()),
]