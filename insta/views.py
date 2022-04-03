import imp
from multiprocessing import context
from django.shortcuts import redirect, render
from .models import Image, Comment, Tag
from .forms import ImageForm
from django.db.models import Q

# Create your views here.
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    images = Image.objects.filter(
       Q(tags__name__icontains = q) |
       Q(owner__username__icontains = q)
    )
    tags = Tag.objects.all()

    if request.GET.get('q') != None:
        images_count = images.count()
    else:
        images_count = -1

    context = {'images': images, 'tags': tags, 'images_count': images_count, }
    return render(request, 'insta/home.html', context)

def post(request, pk):
    image = Image.objects.get(id=pk)
    comments = image.comment_set.all()
    tags = image.tags.all()
    
    context = {'image': image, 'comments':comments, 'tags':tags, }
    return render(request, 'insta/posts.html', context)

def createPost(request): 
    form = ImageForm()

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'insta/post_form.html', context)

def updatePost(request, pk):
    image = Image.objects.get(id=pk)
    form = ImageForm(instance=image)

    if request.method == 'POST':
        form =ImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'insta/post_form.html', context)

def deletePost(request, pk):
    image = Image.objects.get(id=pk)
    if request.method == 'POST':
        image.delete()
        return redirect('home')
    
    context = {'obj':image}
    return render(request, 'insta/delete.html', context)