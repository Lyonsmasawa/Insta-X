from django.contrib import admin
from .models import Image, Comment, Profile, Tag, Follow,Like

# Register your models here.
admin.site.register(Tag)
admin.site.register(Image)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(Follow)
admin.site.register(Like)