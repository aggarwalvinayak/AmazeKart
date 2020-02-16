from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404

from django.http import HttpResponse

from django.contrib import messages
import json
# from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth import logout, authenticate, login

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register(request):
    if request.method == "POST":
        print()
        print(request.POST)
        print()
        print()
        f_email = request.POST.get('email')
        f_password = request.POST.get('password')
        f_fname = request.POST.get('firstname')
        f_lname = request.POST.get('lastname')
        f_phoneno = request.POST.get('phoneno')
        print(f_email,f_password,f_fname,f_lname,f_phoneno)
        try:
            user,created = CustomUser.objects.get_or_create(email = f_email,password = f_password,firstname = f_fname,lastname = f_lname,phoneno = f_phoneno)
            user.set_password(f_password)
            user.save()

            messages.success(request, f"New account created: {f_email}")
            login(request, user)
            return redirect("/homepage")

        except Exception as e:
            print(e)
            return render(request = request,
                                        template_name = "registration/signup.html",
                                        )

    return render(request = request,
                                template_name = "registration/signup.html",
                                )

@csrf_exempt
def login_request(request):
    if request.method == "POST":

        password = request.POST.get('password')
        email = request.POST.get('email')
        print()
        print(email,password)
        user = authenticate(email=email, password=password)
        contextfrontend={
        'email':email,
        'password':password,
        }
        if user is not None: 
                login(request, user)
                print("User Logged in")
                return redirect("../mainapp/store")

        else:
                print("Invalid User")

        return render(request = request,
                                template_name = "registration/signin.html",
                                context=contextfrontend)
    return render(request = request,
                                template_name = "registration/signin.html")

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("amazekart:homepage")