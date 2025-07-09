from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import SocialPost
from .utils import (
    fetch_facebook_posts,
    fetch_twitter_posts,
    post_to_twitter,
    post_to_facebook
)

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'dashboard/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'dashboard/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')



@login_required
def dashboard_view(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        platform = request.POST.get('platform')

        if platform == "Twitter":
            post_to_twitter(content)
        elif platform == "Facebook":
            post_to_facebook(content)

        SocialPost.objects.create(user=request.user, content=content, platform=platform)
        return redirect('dashboard')

    fb_posts = fetch_facebook_posts()
    tweets = fetch_twitter_posts()
    posts = SocialPost.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'dashboard/dashboard.html', {
        'fb_posts': fb_posts,
        'tweets': tweets,
        'posts': posts,
    })

