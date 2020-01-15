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


	def post(self,request):#only one entry per post request
		# print(response)
		user = request.data.get('simpleform')

		# Create an article from the above data
		serializer = UserDatabaseSerializer(data=user)
		if serializer.is_valid(raise_exception=True):
			user_saved = serializer.save()
		return Response({"success": "User '{}' created successfully".format(user_saved.name)})
