from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm, SignupForm
from django.contrib.auth import get_user_model, authenticate, login as auth_login, logout as auth_logout

# Create your views here.
User = get_user_model()


def home(request):
    return render(request, 'accounts/home.html')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            auth_login(request, user)
            mobile = str(user.mobile)
            return HttpResponse('Logging In...' + mobile)
        else:
            return render(request, 'accounts/login.html', context={'error': 'Improper Form', 'form': form})
    else:
        form = LoginForm()
        return render(request, 'accounts/login.html', context={'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User()
            user.username = request.POST['username']
            user.set_password(request.POST['password'])
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.mobile = request.POST['mobile']
            user.save()
            return HttpResponseRedirect('home')
        else:
            if request.POST['password'] != request.POST['password2']:
                error = 'Passwords Do Not Match'
            else:
                error = 'Username is Taken'
            return render(request, 'accounts/signup.html', context={'error': error, 'form': form})
    else:
        form = SignupForm()
        return render(request, 'accounts/signup.html', context={'form': form})


def logout(request):
    auth_logout(request)

    return HttpResponse('Logged Out Successfully')