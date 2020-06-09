from django import forms
from .models import Project,Profile,Rating

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic', 'bio']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['date_posted','user']


class RatingsForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['design', 'usability', 'content', ]
       