from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Image, Comment, Like, Tag, Profile, Follow
from .forms import ImageForm, ProfileForm, FollowForm, UnFollowForm
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
            Profile.objects.create(user=user,)
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
       Q(name__icontains = q) |
       Q(owner__user__username__icontains = q)
    )

    users = User.objects.all()

    if request.GET.get('q') != None:
        images_count = images.count()
    else:
        images_count = -1

    context = {'images': images, 'images_count': images_count, 'users':users, }
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
    user = Profile.objects.get(id=pk)
    images = user.image_set.all()

    profile = get_object_or_404(Profile, pk=pk)

    whoIsFollowing = Profile.objects.get(user = request.user)
    whoToFollow = Profile.objects.get(id = user.id)
    isFollowing = Follow.objects.filter(followed = whoToFollow, follow = whoIsFollowing) 
    posts_count = images.count()

    if request.method == 'POST':
        if 'follow' in request.POST:
            form = FollowForm(request.POST)
            if form.is_valid():
                form_data = form.save(commit=False)
                form_data.followed = whoToFollow
                form_data.follow = whoIsFollowing
                form_data.save()

                get_followers=Follow.objects.filter(followed=whoToFollow)
                followers_count=len(get_followers)

                whoToFollow.followers = followers_count
                whoToFollow.save()

                get_following=Follow.objects.filter(follow=whoIsFollowing)
                following_count=len(get_following)
                
                whoIsFollowing.following=following_count
                whoIsFollowing.save()

            return redirect('profile', profile.id)
             
        elif 'unfollow' in request.POST:
            form = UnFollowForm(request.POST)
            if form.is_valid():
                form_data = form.save(commit=False)
                form_data = Follow.objects.filter(followed =whoToFollow, follow = whoIsFollowing)
                form_data.delete()                

                get_followers=Follow.objects.filter(followed=whoToFollow)
                followers_count=len(get_followers)

                whoToFollow.followers= followers_count
                whoToFollow.save()

                get_following=Follow.objects.filter(follow = whoIsFollowing)
                following_count=len(get_following)

                whoIsFollowing.following=following_count
                whoIsFollowing.save()

            return redirect('profile', profile.id)
    else:
        follow_form = FollowForm()
        unfollow_form = UnFollowForm()

    context = {'user':user, 'images':images, 'profile':profile, 'unfollow_form':unfollow_form, 'follow_form':follow_form,'isFollowing':isFollowing,'posts_count':posts_count,}
    return render(request, 'insta/profile.html', context)

@login_required(login_url='login')
def createPost(request): 
    form = ImageForm()
    user = request.user.profile

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            new = form.save(commit=False)
            new.owner = user
            new.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'insta/post_form.html', context)

@login_required(login_url='login')
def updatePost(request, pk):
    image = Image.objects.get(id=pk)
    form = ImageForm(instance=image)

    
    if request.user != image.owner.user:
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

    if request.user != image.owner.user:
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
    user = request.user.profile
    form = ProfileForm(instance=user)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
        return redirect('profile', request.user.profile.id)

    context = {'form':form, 'user':user}
    return render(request, 'insta/update_user.html', context)

def likePost(request):
    user = request.user
    if request.method == 'POST':
        image_id = request.POST.get("image_id")
        image_obj = Image.objects.get(id = image_id)

        if user in image_obj.liked.all():
            image_obj.liked.remove(user)
        else:
            image_obj.liked.add(user)

        like, created = Like.objects.get_or_create(user = user, image = image_obj)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        like.save()

    return redirect(request.META.get('HTTP_REFERER'))