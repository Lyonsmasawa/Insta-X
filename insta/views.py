from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Image, Comment, Tag, Profile
from .forms import ImageForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        try:
          user = User.objects.get(username=username)
    
        except:
            messages.error(request, 'user does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or Password')

    context = {'page':page}
    return render(request, 'insta/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'please try again')

    context = {'form': form}
    return render(request, 'insta/login_register.html', context)

@login_required(login_url='login')
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    images = Image.objects.filter(
       Q(tags__name__icontains = q) |
       Q(owner__username__icontains = q)
    )
    tags = Tag.objects.all()
    users = User.objects.all()

    if request.GET.get('q') != None:
        images_count = images.count()
    else:
        images_count = -1

    context = {'images': images, 'tags': tags, 'images_count': images_count, 'users':users, }
    return render(request, 'insta/home.html', context)

@login_required(login_url='login')
def post(request, pk):
    image = Image.objects.get(id=pk)
    comments = image.comment_set.all()
    tags = image.tags.all()

    if request.method == 'POST':
        comment = Comment.objects.create(
            user = request.user,
            image = image,
            body = request.POST.get('body')
        )
        return redirect('post', pk=image.id)
    
    context = {'image': image, 'comments':comments, 'tags':tags,}
    return render(request, 'insta/posts.html', context)

def userProfile(request, pk):
    user = User.objects.get(id=pk)
    images = user.image_set.all()
    
    profile = get_object_or_404(Profile, pk=pk)

    context = {'user':user, 'images':images, 'profile':profile}
    return render(request, 'insta/profile.html', context)

@login_required(login_url='login')
def createPost(request): 
    form = ImageForm()

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'insta/post_form.html', context)

@login_required(login_url='login')
def updatePost(request, pk):
    image = Image.objects.get(id=pk)
    form = ImageForm(instance=image)

    
    if request.user != image.owner:
        return HttpResponse('This method is restricted')
        
    if request.method == 'POST':
        form =ImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'insta/post_form.html', context)

@login_required(login_url='login')
def deletePost(request, pk):
    image = Image.objects.get(id=pk)

    if request.user != image.owner:
        return HttpResponse('This method is restricted')

    if request.method == 'POST':
        image.delete()
        return redirect('home')
    
    context = {'obj':image}
    return render(request, 'insta/delete.html', context)

@login_required(login_url='login')
def deleteComment(request, pk):
    comment = Comment.objects.get(id=pk)

    if request.user != comment.user:
        return HttpResponse('This method is restricted')

    if request.method == 'POST':
        comment.delete()
        return redirect('home')
    
    context = {'obj':comment}
    return render(request, 'insta/delete.html', context)

@login_required(login_url='login')
def updateUser(request):

    context = {}
    return render(request, 'insta/update_user.html', context)