from django.forms import ModelForm
from .models import Image, Profile, Follow
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

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
