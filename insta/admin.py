from django.contrib import admin
from .models import Image, Comment, Tag

# Register your models here.
admin.site.register(Tag)
admin.site.register(Image)
admin.site.register(Comment)