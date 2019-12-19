from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):
    if request.method == 'POST':
        #Sign him up
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request,'account/signup.html',{'error': 'Username already taken!'} )
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],request.POST['email'], password = request.POST['password1'],first_name = request.POST['firstname'],last_name = request.POST['lastname']  )
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, 'account/signup.html', {'error': 'Password Does not match!'} )
    else:

        return render(request, 'account/signup.html' )

def login(request):
    if request.method == 'POST':
        user =  auth.authenticate(username=request.POST['username'], password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'account/login.html',{'error': 'Username or Password Does not match!'} )

    else:
        return render(request, 'account/login.html' )

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
