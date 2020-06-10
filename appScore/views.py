from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Profile, Project, Rating
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, ProjectForm,RatingsForm
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer
from  rest_framework.permissions import IsAuthenticated
from rest_framework import status

def index(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {"projects":projects})



@login_required(login_url='/accounts/login/')
def my_profile(request):
    id=request.user.id
    profile = Profile.objects.get(user_id=id)
    projects = Project.objects.filter(user__id=id)
    username = profile.user.username
    project_number = len(projects)
    
    return render(request, 'my_profile.html',{"profile":profile,"projects":projects,"username":username,"project_number":project_number})

@login_required(login_url='/accounts/login/')
def profile(request,id):

    user = User.objects.get(id=id)
    profile = Profile.objects.get(user__id=id)
    projects = Project.objects.filter(user__id=id)
    username = profile.user.username
    project_number = len(projects)
    
    return render(request, 'profile.html',{"profile":profile,"projects":projects,"user":user,"username":username,"project_number":project_number})

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
            post.user = current_user
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


@login_required(login_url='/accounts/login/')
def display_project(request, id):
    project = Project.objects.get(id = id)
    project_ratings = Rating.objects.filter(project__id=id) 
    design_ratings=[]
    usability_ratings=[]
    content_ratings=[]
    if project_ratings:
        index=len(project_ratings)-1
        project_rating = project_ratings[index]
    else:
        project_rating = None
       
    if request.method == 'POST':
        form = RatingsForm(request.POST)
        if form.is_valid():
            new_rating = form.save(commit=False)
            new_rating.user = request.user
            new_rating.project = project
            avg = (new_rating.design+new_rating.content+new_rating.usability)/3
            new_rating.average = round(avg, 2)
            new_rating.save()
            project_ratings = Rating.objects.filter(project__id=id)
            for i in project_ratings:
                design_ratings.append(i.design)
                usability_ratings.append(i.usability)
                content_ratings.append(i.content)

            new_rating.design_average = round((sum(design_ratings) / len(design_ratings)),2)      
            new_rating.usability_average = round((sum(usability_ratings) / len(usability_ratings)),2)
            new_rating.content_average = round((sum(content_ratings) / len(content_ratings)),2)

            average = (new_rating.design_average + new_rating.usability_average + new_rating.content_average) / 3
            new_rating.average = round(average, 2)
            new_rating.save()
            return redirect("display_project", project.id)
           
    else:
        form = RatingsForm()

    return render(request, "display_project.html", {"project":project,"project_rating":project_rating,"form":form})


class ProfileList(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request,format = None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles,many = True)
        return Response(serializers.data)


class ProjectList(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request, format = None):
        all_projects = Project.get_all_projects()
        serializers = ProjectSerializer(all_projects,many = True)
        return Response(serializers.data)


