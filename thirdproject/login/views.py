from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth.models import User
from django.contrib import auth

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['userpassword']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'home.html', {'error' : 'username or password is incorrect.'})
    else:
        return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['userpassword'] == request.POST['userpassword_confirm']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST["userpassword"])
            auth.login(request, user)
            return redirect('home')
    return render(request, 'signup.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        redirect('home')
    return render(request, 'home.html')

def main(request):
    return render(request, 'main.html')
# Create your views here.