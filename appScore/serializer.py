from rest_framework import serializers
from .models import Project,Profile

class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Project
    fields = ('title','landing_page','description','live_site')

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = ('picture','bio','first_name','last_name')