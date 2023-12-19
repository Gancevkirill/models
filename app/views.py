from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_posts')
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})

def display_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/display_posts.html', {'posts': posts})