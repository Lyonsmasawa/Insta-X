from ast import Mod
from random import choices
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Profile(models.Model):
#     """Model definition for Profile."""

#     # TODO: Define fields here
#     profile_photo = models.ImageField(upload_to = 'profiles/')
#     bio = models.TextField(null=True, blank=True)
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True) #auto_now takes a snapshot everytime a save occures while auto_now_add takes a snapshot only one the first time a save occures
   
#     class Meta:
#         """Meta definition for Profile."""

#         verbose_name = 'Profile'
#         verbose_name_plural = 'Profiles'

#     def __str__(self):
#         """Unicode representation of Profile."""
#         return self.profile_photo

class Image(models.Model):
    """Model definition for Image."""

    # TODO: Define fields here
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'static/images/')
    name = models.CharField(max_length=20)
    caption = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True) #auto_now takes a snapshot everytime a save occures while auto_now_add takes a snapshot only one the first time a save occures
    liked = models.ManyToManyField(User, related_name='likes', default=None, blank=True)

    class Meta:
        """Meta definition for Image."""

        verbose_name = 'Image'
        verbose_name_plural = 'Images'
        ordering = ['-updated', '-created']

    def __str__(self):
        """Unicode representation of Image."""
        return self.name

    @property
    def num_likes(self):
        return self.liked.all().count()

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
        return self.body


LIKE_CHOICES = (
    ('Like', 'Like')
    ('Unlike', 'Unlike')
)

class Like(models.Model):
    """Model definition for Like."""

    # TODO: Define fields here
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES,default='Like', max_length=10)

    class Meta:
        """Meta definition for Like."""

        verbose_name = 'Like'
        verbose_name_plural = 'Likes'

    def __str__(self):
        """Unicode representation of Like."""
        return str(self.image)
