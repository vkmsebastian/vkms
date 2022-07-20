from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login as login_user, logout as logout_user, get_user
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



def index(request):
    return render(request, 'home/index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_user(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'home/login.html', {'error': "Invalid username/password"})
    
    else:
        if get_user(request).is_authenticated is False:
            return render(request, 'home/login.html')
        else:
            return HttpResponseRedirect('/')

def logout(request):
    logout_user(request)
    return HttpResponseRedirect('/login')


def register(request):
    if request.method == 'GET':
        return render(request, 'home/register.html')
    
    elif request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            if user is not None:
                login_user(request, user)
                return HttpResponseRedirect('/')

        return render(request, 'home/register.html', {'form': form})

        
            

