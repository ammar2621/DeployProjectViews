from django.shortcuts import render
from .models import Mentee, Mentor, Blog
from .forms import BlogForm, MenteeForm, MentorForm


# Create your views here.
def index(request):
    return render(request, 'home.html')

def Author(request):
    return render(request, 'author.html')

def listmentor(request):
    mentor = Mentor.objects.all()
    return render(request, 'mentor.html', {'mentors': mentor})


def listmentee(request):
    mentee = Mentee.objects.all()
    return render(request, 'mentee.html', {'mentees': mentee})

def listblog(request):
    blog = Blog.objects.all()
    return render(request, 'blog.html', {'blogs': blog})


def input_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            post = form.save(commit=false)
            post.author = request.user
            post.save()
    else:
        form = BlogForm()
    return render(request, 'input_blog.html', {'form': form})

def input_mentee(request):
    if request.method == "POST":
        form = MenteeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=false)
            post.author = request.user
            post.save()
    else:
        form = MenteeForm()
    return render(request, 'input_mentee.html', {'form': form})


def input_mentor(request):
    if request.method == "POST":
        form = MentorForm(request.POST)
        if form.is_valid():
            post = form.save(commit=false)
            post.author = request.user
            post.save()
    else:
        form = MentorForm()
    return render(request, 'input_mentor.html', {'form': form})


def blog_detail(request, blog_id):
    try:
        blog = Blog.objects.get(pk=blog_id)
    except Blog.DoesNotExist:
        raise Http404('Blog does not exist')
    return render(request, 'blog_detail.html', {'blog': blog})