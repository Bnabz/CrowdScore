from django import forms
from .models import Project,Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
       