from django.forms import ModelForm
from .models import Image, Profile, Follow

class ImageForm(ModelForm):
    """Form definition for Image."""

    class Meta:
        """Meta definition for Imageform."""

        model = Image
        fields = '__all__'
        exclude = ['owner']

class ProfileForm(ModelForm):
    """Form definition for Profile."""

    class Meta:
        """Meta definition for Profileform."""

        model = Profile
        fields = '__all__'
        exclude = ['user', 'followers', 'following',]

class FollowForm(ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Follow
        fields = '__all__'
        exclude = ['follow', 'followed']

class UnFollowForm(ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Follow
        fields = '__all__'
        exclude = ['follow', 'followed']
