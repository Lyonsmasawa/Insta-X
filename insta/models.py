from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Profile(models.Model):
    """Model definition for Profile."""

    # TODO: Define fields here
    profile_photo = models.ImageField(upload_to = 'profiles')
    bio = models.CharField(max_length=200)

    class Meta:
        """Meta definition for Profile."""

        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        """Unicode representation of Profile."""
        self.profile_photo
