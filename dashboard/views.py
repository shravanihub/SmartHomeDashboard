from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponseNotAllowed

from .models import *

import boto3


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


ACCESS_KEY = 'AKIAWPJRVS2XKEAJWB7F'
SECRET_KEY = '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'

client = boto3.client(
    'iot',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    region_name='us-east-1'
)


# Create your views here.

def devices(request):
    if request.method == 'GET':
        resp = client.list_things()
        things = resp['things']
        return render(request, template_name="devices.html", context=locals())
    return HttpResponseNotAllowed()
