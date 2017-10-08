from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.template import RequestContext

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


def login(request):
    c = {}
    return render(request, "login.html", c)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    logger.info("---------------------------------------------------- username = " + username)
    logger.info("---------------------------------------------------- password = " + password)
    user = auth.authenticate(username=username, password=password)

    if user is None:
        return HttpResponseRedirect('/accounts/invalid')
    else:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')


def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')


def loggedin(request):
    return render_to_response('loggedin.html')


def invalid_login(request):
    return render_to_response('invalid.html')
