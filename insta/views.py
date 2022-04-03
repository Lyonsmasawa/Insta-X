from multiprocessing import context
from unicodedata import name
from django.shortcuts import render

# Create your views here.
def home(request):
    posts = [
        {'id': 1, 'name': 'Design with me'},
        {'id': 1, 'name': 'Design with me'},
        {'id': 1, 'name': 'Design with me'},
    ]
    context = {'posts': posts}
    return render(request, 'insta/home.html', context)

def post(request):

    context = {}
    return render(request, 'insta/posts.html', context)