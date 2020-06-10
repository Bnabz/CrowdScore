from rest_framework import serializers
from .models import Project,Profile

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = ('user''profile_pic','bio',)

class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Project
    fields = ('title','description','user','link')