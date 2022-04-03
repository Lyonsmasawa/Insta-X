from multiprocessing import context
from unicodedata import name
from django.shortcuts import render

# Create your views here.

posts = [
    {'id': 1, 'name': 'Design with me'},
    {'id': 1, 'name': 'Design with me'},
    {'id': 1, 'name': 'Design with me'},
]

def home(request):
    context = {'posts': posts}
    return render(request, 'insta/home.html', context)

def post(request, pk):
    post = None
    for i in posts:
        if i['id'] == int(pk):
            post = i

    context = {'post':post}
    return render(request, 'insta/posts.html', context)