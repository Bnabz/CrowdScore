from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='images/')
    bio =  models.TextField(blank=True)
    contact = models.CharField(max_length=80 ,null=True)

    def __str__(self):
            return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

