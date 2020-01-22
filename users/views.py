from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404

from django.http import HttpResponse

from django.contrib import messages

# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import logout, authenticate, login

from django.views.decorators.csrf import csrf_exempt


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
                user = form.save()
                email = form.cleaned_data.get('email')
                messages.success(request, f"New account created: {email}")
                login(request, user)
                return redirect("/homepage")

        else:
                for msg in form.error_messages:
                        messages.error(request, f"{msg}: {form.error_messages[msg]}")

                return render(request = request,
                                            template_name = "amazekart/register.html",
                                            context={"form":form})

    form = CustomUserCreationForm
    return render(request = request,
                                template_name = "amazekart/register.html",
                                context={"form":form})
@csrf_exempt
def login_request(request):
    if request.method == "POST":

        password = request.POST.get('password')
        email = request.POST.get('email')
        print()
        print(username,password)
        user = authenticate(email=email, password=password)
        contextfrontend={
        'email':email,
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
    return render(request = request,
                                template_name = "amazekart/login/login.html")

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("amazekart:homepage")