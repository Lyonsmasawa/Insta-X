from django.test import TestCase
from django.contrib.auth.models import User
from .models import Image, Profile

# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.new_obj = User(username = "new_obj", email = "new_obj@gmail.com",password = "pass")
        self.profile = Profile(bio='bio', user= self.new_obj)
        self.new_obj.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_obj, User))
        self.assertTrue(isinstance(self.profile, Profile))

class ImageTestClass(TestCase):
    def setUp(self):
        self.new_obj = User(username = "new_obj", email = "new_obj@gmail.com",password = "pass")
        self.profile = Profile(bio='bio', user= self.new_obj)

        self.img = Image(image = 'imageurl', name ='img', caption = 'img-cap', profile = self.profile)
        
        self.new_obj.save()
        self.profile.save()
        self.img.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.img, Image))
