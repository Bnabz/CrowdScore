from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.urls import reverse


def index(request):
   
    return render(request, 'index.html', {})

