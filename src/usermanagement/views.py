from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template import RequestContext

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


def login(request):
    return render(request, "login.html")


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is None:
        return HttpResponseRedirect('/accounts/invalid')
    else:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')


def logout(request):
    auth.logout(request)
    context = {"msg": {"ok": "Logged out correctly, see you soon ;)"}}
    return render(request, 'login.html', context)


def loggedin(request):
    context = {"logged": True}
    return render(request, 'index.html', context)


def invalid_login(request):
    context = {"msg": {"error": "User or password invalid!"}}
    return render(request, 'login.html', context)
