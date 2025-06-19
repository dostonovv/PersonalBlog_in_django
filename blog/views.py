from ipaddress import ip_address

from django.db.models.expressions import result
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
from datetime import date
from django.db.models import Q

def post_detail(request , pk):
    """viewga +=1"""
    post = get_object_or_404(Post , pk=pk)
    post.views+=1
    post.save(update_fields=['views'])
    return render(request , 'blog/post_detail.html' , {'post' : post})
def home_page(request):
    posts = Post.objects.all().order_by('-created_at')
    print('Postlar:', posts)
    return render(request, 'blog/home.html', {'posts': posts})

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'posts': posts})
def about(request):
    return render(request, 'blog/about.html')

def today_posts(request):
    today = timezone.now().date()
    posts = Post.objects.filter(created_at__date=today)
    return render(request, 'blog/today.html', {'posts': posts})

def top_posts(request):
    top_posts = Post.objects.order_by('-views')
    return render(request, 'blog/top.html', {'top_posts': top_posts})


def search_results(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Post.objects.filter(
            Q(title__icontains = query) |
            Q(body1__icontains = query)
        ).order_by('-created_at')
    return render(request , 'blog/search_results.html' , {'query' : query , 'results' : results})

