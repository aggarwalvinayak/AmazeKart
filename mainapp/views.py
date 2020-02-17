from django.shortcuts import render,redirect
import json
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
from django.contrib.auth import authenticate,login
import os
from users.models import CustomUser
import time
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, renderer_classes
from django.http import JsonResponse

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

@csrf_exempt
def Upload(request):
	productname = request.POST.get('name')
	productcat = request.POST.get('cat')
	productprice = request.POST.get('price')
	productdesc = request.POST.get('desc')
	print(productname)
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
		product=Product(productname=productname,price=productprice,description=productdesc,user=request.user)
		product.save()
		for image in image_urls:
			img=Image(imageurl=image,product=product)
			img.save()
		return HttpResponse("File(s) uploaded!")
	else:
		return HttpResponse("Please login before selling a product")


class ProductList(APIView):

	def get(self,request):
		search = request.GET.get('search')
		category = request.GET.get('cat')
		sort = request.GET.get('sort')
		email = request.GET.get('email')
		user1 = request.GET.get('user')
		if(user1):
			if request.user.is_authenticated:
				user_selling=Product.objects.filter(user=request.user)
				serializer = ProductSerializer(user_selling,many = True)
				return Response(serializer.data)

			else:
				return HttpResponse("Please Login to view this .")
		if(email):
			uss = CustomUser.objects.get(email=email)
			user_selling=Product.objects.filter(user=uss)
			serializer = ProductSerializer(user_selling,many = True)
			return Response(serializer.data)	

		if(category and category!='All'):
			cat_filter=Product.objects.filter(category=category)
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
			

		# print(search_filter)
		product_list = search_filter
		serializer = ProductSerializer(product_list,many = True)

		return Response(serializer.data)


	def post(self,request):#only one entry per post request
		productname = request.POST.get('name')
		productcat = request.POST.get('cat')
		productprice = request.POST.get('price')
		productdesc = request.POST.get('desc')
		image_urls=request.POST.get('image')
		email=request.POST.get('email')
		print(image_urls)
		product=Product(productid=1,productname=productname,category=productcat,price=productprice,description=productdesc,user=CustomUser.objects.get(email=email))
		product.save()
		image_urls=image_urls[1:-1].split(',')
		if(image_urls):
			for image in image_urls:
				img=Image(imageid=1,imageurl=image.strip(),product=product)
				img.save()
		else:
			img=Image(imageid=1,imageurl="https://www.lbsnaa.gov.in/upload/academy_souvenir/images/59031ff5e92caNo-image-available.jpg",product=product)
			img.save()
		return Response("File(s) uploaded!")

@csrf_exempt
def LoginApi(request):
	
	if request.method == "POST":

		# dataa = request.body.decode('utf-8')
		# dataaa=json.loads(dataa)
		# email=dataaa['email']
		# password = dataaa['password']
		email=request.POST.get('email')
		password=request.POST.get('password')

		print()
		print(email,password)
		user = authenticate(email=email, password=password)
		
		if user is not None: 
				login(request, user)
				print("User Logged in")
				contextfrontend  = {"email":user.email,"firstname":user.firstname,
					"lastname":user.lastname,"phoneno":user.phoneno}
				return JsonResponse(contextfrontend, status=200)
		else:
				print("Invalid User")

		return JsonResponse({'F':'F'}, status=200)
	return JsonResponse({'F':'F'}, status=200)

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

			user = authenticate(username=f_email, password=f_password)

			if user is not None:
				login(user,request)
				return Response({"Success"})
			else:
				return Response({"F"})
		except Exception as e:
			print(e)

		return Response({"F"})

class UpdateApi(APIView):
	
	def get(self,request):
		return Response("Update/Delete APIView")

	def post(self,request):
		productid = request.data.get('id')
		email = request.data.get('email')
		productname = request.data.get('productname')
		price = request.data.get('price')
		category = request.data.get('category')
		description = request.data.get('description')
		delete = request.data.get('delete')

		product_object = Product.objects.get(pk = productid)
		if product_object.user.email!=email:
			return Response({"Failure"})

		if delete == "true":
			product_object.delete()
		else:
			product_object.productname = productname
			product_object.price = price
			product_object.category = category
			product_object.description = description
			product_object.save()

		return Response({"Success"})


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