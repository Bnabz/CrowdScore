from django.test import TestCase
from .models import User,Profile,Project,Rating
from django.contrib.auth.models import User

class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User(username="test_name2", password = "test_pass",email="testmail@gmail.com")
        self.user.save()
        self.profile = Profile(user=self.user, profile_pic='test.jpg',bio="test_bio")
        self.profile.save()


    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile)) 


    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()

class ProjectTestCase(TestCase):
    def setUp(self):
        self.user = User(username="test_name", password = "test_pass",email="testmail@gmail.com")
        self.user.save()
        self.profile = Profile(user=self.user, profile_pic='test.jpg',bio="test_bio",)
        self.profile.save()
        self.project_test = Project(name="test_project", caption="test_caption", user = self.user, profile=self.profile)                     
        self.project_test.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.project_test, Project))

    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
        Project.objects.all().delete()
