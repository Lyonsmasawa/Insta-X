from ast import Mod
from pyexpat import model
from random import choices
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    """Model definition for Profile."""

    # TODO: Define fields here
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to = 'profiles/')
    bio = models.TextField(null=True, blank=True)
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True) #auto_now takes a snapshot everytime a save occures while auto_now_add takes a snapshot only one the first time a save occures
   
    class Meta:
        """Meta definition for Profile."""

        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        """Unicode representation of Profile."""
        return self.user.username

class Tag(models.Model):
    """Model definition for Tag."""

    # TODO: Define fields here
    name = models.CharField(max_length=30)

    class Meta:
        """Meta definition for Tag."""

        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        """Unicode representation of Tag."""
        return self.name

class Image(models.Model):
    """Model definition for Image."""

    # TODO: Define fields here
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'static/images/')
    tags = models.ManyToManyField(Tag)
    name = models.CharField(max_length=20)
    caption = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True) #auto_now takes a snapshot everytime a save occures while auto_now_add takes a snapshot only one the first time a save occures
    # likes = models.ManyToManyField(User, related_name='likes', default=None, blank=True)

    class Meta:
        """Meta definition for Image."""

        verbose_name = 'Image'
        verbose_name_plural = 'Images'
        ordering = ['-updated', '-created']

    def __str__(self):
        """Unicode representation of Image."""
        return self.name

class Comment(models.Model):
    """Model definition for Comment."""

    # TODO: Define fields here
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True) #auto_now takes a snapshot everytime a save occures while auto_now_add takes a snapshot only one the first time a save occures


    class Meta:
        """Meta definition for Comment."""

        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['-updated', '-created']

    def __str__(self):
        """Unicode representation of Comment."""
        return self.body[0:50]

# class Follower(models.Model):
#     """Model definition for Follower."""

#     # TODO: Define fields here
#     Follower
#     class Meta:
#         """Meta definition for Follower."""

#         verbose_name = 'Follower'
#         verbose_name_plural = 'Followers'

#     def __str__(self):
#         """Unicode representation of Follower."""
#         pass
