from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404

from django.http import HttpResponse

from django.contrib import messages

# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, authenticate, login

from django.views.decorators.csrf import csrf_exempt


