from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Profile(models.Model):
    """Model definition for Profile."""

    # TODO: Define fields here
    profile_photo = models.ImageField(upload_to = 'profiles/')
    bio = models.CharField(max_length=200)

    class Meta:
        """Meta definition for Profile."""

        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        """Unicode representation of Profile."""
        self.profile_photo

class Image(models.Model):
    """Model definition for Image."""

    # TODO: Define fields here
    image = models.ImageField(upload_to = 'posts/')
    name = models.CharField(max_length=20)
    caption = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Image."""

        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        """Unicode representation of Image."""
        pass
