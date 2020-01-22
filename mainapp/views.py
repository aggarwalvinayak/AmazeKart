from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Image,Product
from . serializers import ProductSerializer,ImageSerializer
import requests

class ProductList(APIView):

	def get(self,request):
		search = request.GET.get('search')
		category = request.GET.get('cat')
		sort = request.GET.get('sort')
		print("YAASS",search,category,sort)
		product_list = Product.objects.all()
		serializer = ProductSerializer(product_list,many = True)

		return Response(serializer.data)


	def post(self,request):#only one entry per post request
		# print(response)
		product = request.data.get('product')
		# Create an article from the above data
		serializer = ProductSerializer(data=product)
		if serializer.is_valid(raise_exception=True):
			product_saved = serializer.save()
		return Response({"success": "Product '{}' created successfully".format(product_saved.productname)})



class ImageList(APIView):
	
	def get(self,request):

		image_list = Image.objects.all()
		serializer = ImageSerializer(image_list,many = True)

		return Response(serializer.data)


	def post(self,request):#only one entry per post request
		# print(response)
		image = request.data.get('image')

		# Create an article from the above data
		serializer = ImageSerializer(data=image)
		if serializer.is_valid(raise_exception=True):
			image_saved = serializer.save()
		return Response({"success": "Image '{}' created successfully".format(image_saved.imageid)})

def store(request):
	search = request.GET.get('search')
	category = request.GET.get('cat')
	sort = request.GET.get('sort')
	# print(search,category,sort)
	param={'search':search,'cat':category,"sort":sort}
	getdata = requests.get('http://127.0.0.1:8000/mainapp/productdatabase/',params=param)

	# listdata=

	return render(request = request,
								template_name = "mainapp/store.html")