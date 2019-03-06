from django.shortcuts import render
from .models import Blog
from .models import Score
from django.core.paginator import Paginator

from django.shortcuts import redirect

from django.contrib.auth.models import User
from django.contrib import auth

def login(request):
    success = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['userpassword']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            success = 'true'
            return redirect('home')
        else:
            return render(request, 'login.html', {'error' : 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def home(request):
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'posts':posts})

    

def join(request):
    if request.method == 'POST':
        if request.POST['userpassword'] == request.POST['userpassword_confirm']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST["userpassword"])
            auth.login(request, user)
            return redirect('login')
    return render(request, 'join.html')