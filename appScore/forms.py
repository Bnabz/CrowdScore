from django import forms
from .models import Project,Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        fields = ['profile_pic', 'bio']

class ProjectForm(forms.ModelForm):
    class Meta:
        exclude = ['date_posted']
       