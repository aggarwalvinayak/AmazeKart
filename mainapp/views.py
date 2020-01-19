from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from . models import User
# from . serializers import UserSerializer


# class UserList(APIView):

# 	def get(self,request):

# 		users_list = User.objects.all()
# 		serializer = UserSerializer(users_list,many = True)

# 		return Response(serializer.data)


# 	def post(self,request):#only one entry per post request
# 		# print(response)
# 		user = request.data.get('simpleform')

# 		# Create an article from the above data
# 		serializer = UserSerializer(data=user)
# 		if serializer.is_valid(raise_exception=True):
# 			user_saved = serializer.save()
# 		return Response({"success": "User '{}' created successfully".format(user_saved.name)})

class ProductList(APIView):
	pass

class ImageList(APIView):
	pass
