from django.shortcuts import redirect, render
from .models import Image, Comment, Tag
from .forms import ImageForm

# Create your views here.
def home(request):
    images = Image.objects.all()

    context = {'images': images}
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