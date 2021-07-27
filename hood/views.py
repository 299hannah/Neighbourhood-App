from hood.forms import  *
from django.http import request
from django.http.response import HttpResponseRedirect

from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from .models import Profile,Post
# Create your views here.

def logout(request):
    logout(request)
    return redirect('login')

def index(request):
    hoods =Neighbourhood.objects.all()
    business=Business.objects.all()
    context={
        'hoods':hoods,
        'business':business
    }
    return render(request,'index.html', context)


def profile(request, username):
    user=User.objects.get(username=username)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('update',user.username)

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm()

    context = {
        'user':user,
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
        form = UpdatePostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return redirect('post')
    else:
        form = UpdatePostForm(instance=post)
            
    
    return render(request,'update_post.html',{'form':form})

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
            return redirect('newhood')
            
    else:
        form = CategoryForm()
        
    return render(request, 'category.html', {'form':form})

def create_hood(request):
    if request.method == 'POST':
        form = NeighbourHoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.save()
            return redirect('index')

    else:
        form = NeighbourHoodForm()
    return render(request, 'neighbourhood.html', {'form': form})

def hood(request):
    hoods = Neighbourhood.objects.all()
    
    return render(request, 'index.html',{'hoods':hoods})

def join_hood(request, id):
    neighbourhood = get_object_or_404(Neighbourhood, id=id)
    request.user.profile.neighbourhood = neighbourhood
    request.user.profile.save()
    return render(request, 'neighbourhood.html')

def leave_hood(request, id):
    hood = get_object_or_404(Neighbourhood, id=id)
    request.user.profile.neighbourhood = None
    request.user.profile.save()
    return render(request, 'neighbourhood.html')

def search_results(request):
    if 'name' in request.GET and request.GET["name"]:
        search_term = request.GET.get("name")
        searched_names = Business.search_by_name(search_term)

        message = f"{search_term}"
        

        return render (request, 'search.html',{"message":message,"names": searched_names})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})



