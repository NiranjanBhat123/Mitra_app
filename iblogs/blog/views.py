from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post, Category, Updates, Teachers, Uploads
from django.core.files.storage import FileSystemStorage


# Create your views here.


def home(request):
    # load the posts from db
    posts = Post.objects.all()[21:]
    cats = Category.objects.all()
    updates = Updates.objects.all()
    
    data = {
        'posts': posts,
        'cats': cats,
        'updates': updates,
    }
    return render(request, 'home.html', data)


def viewmore(request):
    posts = Post.objects.all()[0:21]
    cats = Category.objects.all()
    updates = Updates.objects.all()
    
    data = {
        'posts': posts,
        'cats': cats,
        'updates': updates,
    }
    return render(request, 'viewmore.html', data)


def post(request, url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()
    
    return render(request, 'posts.html', {'post': post, 'cats': cats})


def category(request, url):
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    return render(request, 'category.html', {'cat': cat, 'posts': posts})


def updates(request, url):
    up = Updates.objects.get(url=url)
    ups = Updates.objects.all()
    return render(request, 'updates.html', {'up': up, 'ups': ups})


def teachers(request):
    teachers = Teachers.objects.all()
    return render(request, 'teachers.html', {'teachers': teachers})


def homework(request):
    return render(request, 'homework.html', {})


def upload(request):
    if request.method == "POST":
        name = request.POST['name']
        section = request.POST['section']
        roll = request.POST['roll']
        subject = request.POST['subject']
        image =  request.FILES['image']
        new_work = Uploads(name=name,standard=section,roll_no= roll,subject=subject,image = image)
        new_work.save()
        return render(request,'success.html',{})
        
        
        
        

    
