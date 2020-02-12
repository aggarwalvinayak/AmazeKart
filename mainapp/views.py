from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Image,Product
from . serializers import ProductSerializer
import requests
from .models import Product,Image
import json
from os import listdir
from os.path import isfile, join
from django.contrib.auth import authenticate
import os
from users.models import CustomUser
import time

def firebaseup():
	from google.cloud import storage
	from datetime import timedelta

	client=storage.Client()
	bucket=client.get_bucket('amazekart-bits.appspot.com')

	url=[]
	onlyfiles = [f for f in listdir("./media/") if isfile(join("./media", f))]

	for f in onlyfiles:
		# print(f)
		imageBlob = bucket.blob("/Product/")

		imageBlob=bucket.blob("img"+str(int(round(time.time() * 1000))))
		imageBlob.upload_from_filename("./media/"+str(f))
		os.remove("./media/"+f)
		url.append(imageBlob.generate_signed_url(expiration=timedelta(300)))
	print(url)
	return url

def Form(request):
	return render(request, "mainapp/image_form.html", {})

def Upload(request):
	productname = request.POST.get('name')
	productcat = request.POST.get('cat')
	productprice = request.POST.get('price')
	productdesc = request.POST.get('desc')
	if request.user.is_authenticated:
		for count, x in enumerate(request.FILES.getlist("files")):
			def process(f):
				with open('./media/' + str(count), 'wb+') as destination:
					# print('hello')
					for chunk in f.chunks():
						destination.write(chunk)
				destination.close()
			process(x)
		image_urls=firebaseup()
		product=Product(productid=1,productname=productname,price=productprice,description=productdesc,user=request.user)
		product.save()
		for image in image_urls:
			img=Image(imageid=1,imageurl=image,product=product)
			img.save()
		return HttpResponse("File(s) uploaded!")
	else:
		return HttpResponse("Please login before selling a product")


class ProductList(APIView):

	def get(self,request):
		search = request.GET.get('search')
		category = request.GET.get('cat')
		sort = request.GET.get('sort')
		# print("YAASS",search,category,sort)
		if(category and category!='All'):
			cat_filter=Product.objects.filter(category='Electronics')
		else:
			cat_filter=Product.objects.all()
		if(search):
			temp1=cat_filter.filter(productname__icontains=search)
			temp2=cat_filter.filter(description__icontains=search)
			search_filter=temp1
			search_filter=search_filter.union(temp2)
			for word in search.split():
				temp1=cat_filter.filter(productname__icontains=word)
				temp2=cat_filter.filter(description__icontains=word)
				search_filter=search_filter.union(temp1)
				search_filter=search_filter.union(temp2)
		else:
			search_filter=cat_filter
			

		print(search_filter)
		product_list = search_filter
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



class LoginApi(APIView):
	
	def get(self,request):
		return Response("LoginAuth APIView")

	def post(self,request):
		username = request.data.get('email')
		password = request.data.get('password')

		print(username,password)

		user = authenticate(username=username, password=password)

		if user is not None:
			return Response({"Success"})

		else:
			return Response({"Failure"})

class RegisterApi(APIView):
	
	def get(self,request):
		return Response("Register APIView")

	def post(self,request):
		f_email = request.data.get('email')
		f_password = request.data.get('password')
		f_fname = request.data.get('firstname')
		f_lname = request.data.get('lastname')
		f_phoneno = request.data.get('phoneno')

		try:
			user,created = CustomUser.objects.get_or_create(email = f_email,password = f_password,firstname = f_fname,lastname = f_lname,phoneno = f_phoneno)
			user.set_password(f_password)
			user.save()
			return Response({"Success"})

		except Exception as e:
			print(e)

		return Response({"Failure"})


def store(request):
	search = request.GET.get('search')
	category = request.GET.get('cat')
	sort = request.GET.get('sort')
	# print(search,category,sort)
	param={'search':search,'cat':category,"sort":sort}
	getdata = requests.get('http://127.0.0.1:8000/mainapp/productdatabase/',params=param)
	data=getdata.json()
	# print(11,getdata.json()[0]['productname'])
	# data=json.loads(json)
	print(getdata)
	contextfrontend={'data':data}

	return render(request = request,
								template_name = "mainapp/store.html",context=contextfrontend)