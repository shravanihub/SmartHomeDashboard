

from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout

from .models import *

# Create your views here.


def index(request):
    return render(request, "index.html")


@require_http_methods(["GET", "POST"])
def useLogin(request):
    if request.method == 'GET':
         return render(request, "login.html")

    if request.method == 'POST':
        username = request.POST.get('username')
        passwd = request.POST.get('password')
        user = authenticate(request, username=username, password=passwd)
        if user is not None:
            login(request, user)
        else:
            status_msg = 'Invalid Credentials'
            return render(request, 'login.html', locals())
        return redirect('/index')

