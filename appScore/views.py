from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Profile, Project
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.urls import reverse


def index(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {"projects":projects})



@login_required(login_url='/accounts/login/')
def my_profile(request):
    current_user = request.user
    id=request.user.id 
    profile = Profile.objects.get(id=id)
    projects = Project.objects.filter(user__id=id)
    username = profile.user.username
    project_number = len(projects)
    

    return render(request, 'my_profile.html',{"profile":profile,"projects":projects,"username":username,"project_number":project_number})