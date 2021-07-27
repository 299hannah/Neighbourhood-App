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
    hoods =Neighbourhood.objects.all()
    business=Business.objects.all()
    context={
        'hoods':hoods,
        'business':business
    }
    return render(request,'index.html', context)


def update_profile(request):
    profile=Profile.objects.get(user=request.user) 
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('update')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'profile':profile,
    }
    
  
    return render(request, 'update_profile.html',context)

def profile(request):
    profile=Profile.objects.get(user=request.user)
    # print(user)
    
    ctx={
        'profile':profile,
    }
    return render(request, 'profile.html', ctx)


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
    # profile = request.user.email
 
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = current_user
            # post.author_profile = profile
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

def business(request):
    businesses = Business.objects.all()
    
    return render(request, 'business.html',{'businesses':businesses})


def update(request):

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



def search_business(request):
    """ search function  """
    if request.method == "POST":
        query_name = request.POST.get('name', None)
        if query_name:
            results = Business.objects.filter(name__contains=query_name)
            return render(request, 'search.html', {"results":results})
    return render(request, 'search.html')

# def search_results(request):
#     if 'name' in request.GET and request.GET["name"]:
#         search_term = request.GET.get("name")
#         searched_businesses = Business.search_by_name(search_term)

#         message = f"{search_term}"
        

#         return render (request, 'search.html',{"message":message,"name": searched_businesses})

#     else:
#         message = "You haven't searched for any term"
#         return render(request, 'search.html',{"message":message})

def detail(request):
    details = Neighbourhood.objects.all()
    
    return render(request, 'index.html',{'details':details})





