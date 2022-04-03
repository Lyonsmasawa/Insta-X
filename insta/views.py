from multiprocessing import context
from unicodedata import name
from django.shortcuts import render
from .models import Image, Comment

# Create your views here.
def home(request):
    images = Image.objects.all()

    context = {'images': images}
    return render(request, 'insta/home.html', context)

def post(request, pk):
    image = Image.objects.get(id=pk)
    comments = image.comment_set.all()
    
    context = {'image': image, 'comments':comments}
    return render(request, 'insta/posts.html', context)