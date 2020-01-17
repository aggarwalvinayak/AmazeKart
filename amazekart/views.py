from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404

from django.http import HttpResponse

from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, authenticate, login

def register(request):
		if request.method == "POST":
				form = UserCreationForm(request.POST)
				if form.is_valid():
						user = form.save()
						username = form.cleaned_data.get('username')
						messages.success(request, f"New account created: {username}")
						login(request, user)
						return redirect("homepage.html")

				else:
						for msg in form.error_messages:
								messages.error(request, f"{msg}: {form.error_messages[msg]}")

						return render(request = request,
													template_name = "amazekart/register.html",
													context={"form":form})

		form = UserCreationForm
		return render(request = request,
									template_name = "amazekart/register.html",
									context={"form":form})

def login_request(request):
		password = request.POST.get('password')
		username = request.POST.get('username')
		print()
		print(username,password)
		user = authenticate(request, username=username, password=password)
		contextfrontend={
		'username':username,
		'password':password,
		}
		if user is not None: 
				login(request, user)
				print("User Logged in")
				return redirect("homepage.html")

		else:
				print("Invalid User")

		return render(request = request,
									template_name = "amazekart/login/login.html",
									context=contextfrontend)

def logout_request(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect("amazekart:homepage")