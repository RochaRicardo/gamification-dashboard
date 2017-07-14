# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth import authenticate, login

from django.http import HttpResponse

from django.views.decorators.http import require_http_methods



# Create your views here.

@require_http_methods(["GET"])
def index(request):
    #return HttpResponse("Hello, world. You're at the Gamification DASHBOARD index.")
    return render(request, 'index.html')
	
	
@require_http_methods(["POST"])
def signin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
	
    if user is not None:
        login(request,user)
        # Redirect to a success page.
        return HttpResponse("Welcome here %s" % (username))
    else:
        # Return an 'invalid login' error message.
        return HttpResponse("We don't recognise you :/")