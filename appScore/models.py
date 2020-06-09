from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator,MaxValueValidator
from statistics import mean

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='images/')
    bio =  models.TextField(blank=True)
    
    def __str__(self):
        return f'{self.user.username}'

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    
    @receiver(post_save, sender = User)
    def create_profile(sender, instance,created, **kwargs):
        if created:
            Profile.objects.create(user = instance)

    @receiver(post_save,sender = User)
    def save_profile( sender, instance, **kwargs):
        instance.profile.save()    

class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True, blank=True)
    screenshot = models.ImageField(upload_to='images/')
    link = models.URLField(max_length=250)

    def __str__(self):
        return self.title
    

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def search_project(cls, name):
        return cls.objects.filter(title__icontains=name).all()


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    design = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    usability = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], null=True)
    content = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    average = models.DecimalField(decimal_places=2)

    def save_rate(self):
        self.save()

    def delete_rate(self):
        self.delete()



