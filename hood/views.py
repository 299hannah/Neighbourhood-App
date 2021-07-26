from hood.forms import  *
from django.http import request
from django.http.response import HttpResponseRedirect

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile,Post
# Create your views here.

def logout(request):
    logout(request)
    return redirect('login')

def index(request):
    posts = Post.objects.all()
    context={
        'posts':posts,
    }
    return render(request,'index.html', context)


def profile(request, username):
    user=User.objects.get(username=username)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('update',user.username)

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)


def new_business(request):
    current_user = request.user

    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.User = current_user
            project.save()
        return redirect('index')

    else:
        form = BusinessForm()
    return render(request, 'new_business.html', {"form": form})

def new_post(request):
    current_user = request.user
    profile = request.user.email
 
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = current_user
            post.author_profile = profile
            post.save()
        return redirect('post')

    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form})

def update_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "post":
        update_post_form = UpdatePostForm(request.POST,request.FILES,instance=post)
        if update_post_form.is_valid():
            update_post_form.save()
            return redirect('post')
    else:
        update_post_form = UpdatePostForm(instance=post)
            
    
    return redirect(request,'update_post.html',{'update_post_form':update_post_form})

def get_post(request, pk):
	post = Post.objects.get(pk=pk)

	context = {
	'post':post
	}
	return render(request, 'detail_post.html', context)

def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    
    
    return redirect('post')

def post(request):
    posts = Post.objects.all()
    
    return render(request, 'posts.html',{'posts':posts})


def update(request,username):

	return render(request, 'update.html')


def category(request):
    # name=Category.objects.all()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
            
    else:
        form = CategoryForm()
        
    return render(request, 'category.html', {'form':form})

def create_hood(request):
    if request.method == 'POST':
        form = NeighbourHoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user.profile
            hood.save()
    else:
        form = NeighbourHoodForm()
    return render(request, 'neighbourhood.html', {'form': form})

