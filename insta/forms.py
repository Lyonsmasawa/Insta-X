from django.forms import ModelForm
from .models import Image

class ImageForm(ModelForm):
    """Form definition for Image."""

    class Meta:
        """Meta definition for Imageform."""

        model = Image
        fields = '__all__'
        # exclude = ['owner']

