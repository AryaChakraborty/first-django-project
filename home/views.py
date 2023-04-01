from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from datetime import datetime
from home.models import Contact, Blogs
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from .models import Blogs

# Create your views here.
@login_required
def index(request) :
    # context is the set of variables u are using in the frontend
    # context = {
    #     "name" : "Arya"
    # }
    if request.user.is_anonymous :
        return redirect('/login')
    return render(request, 'index.html')

@login_required
def about(request) :
    return render(request, 'about.html')

# write blogs
@login_required
def blogs(request) :
    if request.method == 'POST' :
        username = request.user.username
        title = request.POST.get('title')
        blog = request.POST.get('blog')
        date = datetime.today()
        blog_instance = Blogs(username=username, title=title, blog=blog, date=date)
        blog_instance.save()
        messages.success(request, "your blog has been published")
    return render(request, 'blogs.html')
# see all blogs
@login_required
def blog_view(request) :
    # write the code for showing all blogs in the website
    all_blogs = Blogs.objects.all()
    blogs = []
    for blog in all_blogs:
        #
        blogs.append({
            'title': blog.title,
            'content': blog.blog,
            'date': blog.date,
            'author' : blog.username,
            'pk' : blog.pk,
            'edit_info' : (request.user.username == blog.username)
        })
    context = {'blog_data' : blogs}
    return render(request, 'blog_read.html', context)
# see clicked blog
@login_required
def blog_post(request, pk):
    post = get_object_or_404(Blogs, pk=pk)
    context = {'post': post}
    return render(request, 'blog_view.html', context)
# my blogs section
@login_required
def my_blogs(request) :
    your_blogs = Blogs.objects.filter(username=request.user.username)
    your_blogs_to_be_returned = []
    for blog in your_blogs :
        your_blogs_to_be_returned.append({
            'title': blog.title,
            'content': blog.blog,
            'date': blog.date,
            'author': 'you',
            'pk': blog.pk,
            'edit_info': True
        })
    context = {'blog_data': your_blogs_to_be_returned, 'mine' : True}
    return render(request, 'blog_read.html', context)
# edit blog section
@login_required
def edit_blog(request, pk) :
    blog_to_be_edited = Blogs.objects.get(pk=pk)
    context = {
        'title': blog_to_be_edited.title,
        'blog': blog_to_be_edited.blog,
        'pk': pk
    }
    if request.method == 'POST':
        new_title = request.POST.get('new_title')
        blog_to_be_edited.title = new_title
        new_content = request.POST.get('new_content')
        blog_to_be_edited.blog = new_content
        blog_to_be_edited.date = datetime.today()
        blog_to_be_edited.save()
        messages.success(request, "your blog has been edited")
    return render(request, 'edit_blog.html', context)
# delete blog section
def delete_blog(request, pk) :
    blog_to_be_deleted = Blogs.objects.get(pk=pk)
    blog_to_be_deleted.delete()
    all_blogs = Blogs.objects.all()
    blogs = []
    for blog in all_blogs:
        #
        blogs.append({
            'title': blog.title,
            'content': blog.blog,
            'date': blog.date,
            'author': blog.username,
            'pk': blog.pk,
            'edit_info': (request.user.username == blog.username)
        })
    context = {'blog_data': blogs}
    messages.warning(request, 'your blog has been deleted')
    return render(request, 'blog_read.html', context)
# blog search section
@login_required
def blog_view_search(request) :
    if request.method == 'POST':
        title_query = request.POST.get('search_keyword')
        all_blogs = Blogs.objects.filter(title__contains=title_query)
        blogs = []
        for blog in all_blogs:
            #
            blogs.append({
                'title': blog.title,
                'content': blog.blog,
                'date': blog.date,
                'author' : blog.username,
                'pk' : blog.pk,
                'edit_info' : (request.user.username == blog.username)
            })
        context = {'blog_data' : blogs}
    return render(request, 'blog_read_after_search.html', context)

@login_required
def contact(request) :
    if request.method == 'POST' :
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        date = datetime.today()
        contact_instance = Contact(name=name, email=email, phone=phone, desc=desc, date=date)
        contact_instance.save()
        messages.success(request, "your message has been sent")
    return render(request, 'contact.html')

def login_user(request) :
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # check if user gave correct credentials
        user = authenticate(username=username, password=password)
        if user is not None :
            login(request, user)
            return redirect("/")
        else :
            messages.warning(request, "the password or username doesn't match")
            return render(request, 'login.html')
    return render(request, 'login.html')

def logout_user(request) :
    logout(request)
    return redirect("/login")

def is_user_registered(username):
    try:
        User.objects.get(username=username)
        return True
    except:
        return False
def register_user(request) :
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('confirm_password')
        if is_user_registered(username) :
            messages.warning(request, "username is already registered")
            return render(request, 'register.html')
        else :
            if password == password1 :
                new_user = User.objects.create_user(username=username, email=email, password=password)
                print(new_user)
                new_user.save()
                return redirect("/login")
            else :
                # passwords do not match
                messages.warning(request, "the passwords do not match")
                return render(request, 'register.html')
    return render(request, 'register.html')