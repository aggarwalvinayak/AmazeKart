from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import UserDatabase
from . serializers import UserDatabaseSerializer


class UserDatabaseList(APIView):

    def get(self,request):

        users_list = UserDatabase.objects.all()
        serializer = UserDatabaseSerializer(users_list,many = True)

        return Response(serializer.data)


    def post(self):
        pass