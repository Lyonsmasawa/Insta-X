from django.contrib import admin
from .models import Image, Comment, Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(Image)
admin.site.register(Comment)