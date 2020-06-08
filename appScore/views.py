from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Profile, Project
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, ProjectForm
from django.contrib.auth.models import User
from django.urls import reverse


def index(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {"projects":projects})



@login_required(login_url='/accounts/login/')
def my_profile(request):
    id=request.user.id 
    profile = Profile.objects.get(id=id)
    projects = Project.objects.filter(user__id=id)
    username = profile.user.username
    project_number = len(projects)
    

    return render(request, 'my_profile.html',{"profile":profile,"projects":projects,"username":username,"project_number":project_number})

@login_required(login_url='/accounts/login')
def edit_profile(request):

    form=ProfileForm(instance=request.user.profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES,instance=request.user.profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('index')

        else:
            form=ProfileForm()

    return render(request,'edit_profile.html', {"form":form})




@login_required(login_url='/accounts/login/')
def submit_project(request):
    current_user = request.user
    current_profile = Profile.objects.filter(user=current_user)


    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.profile = current_user
            post.likes = 0
            post.save()

        return redirect('index')

    else:
        form = ProjectForm()

    return render(request, 'submit_project.html',{"form":form,"current_profile":current_profile })


def search_results(request):

    if 'searchterm' in request.GET and request.GET['searchterm']:
        search_term = request.GET.get("searchterm")
        searched_name = Project.search_project(search_term)
        
        return render(request,'search.html', { "projects":searched_name,})

    else:
        message = "You haven't searched for any project"
        return render(request,'search.html',{"message":message})


