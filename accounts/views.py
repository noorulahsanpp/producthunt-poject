from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def signup(request):
    if request.method == 'POST':
        #User has info and wants an account
        if request.POST['password'] == request.POST['cpassword']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Username has already taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Password does not match'})
    else :
        #User wants to entet info
        return render(request, 'accounts/signup.html')


def login(request):
    return render(request, 'accounts/login.html')
