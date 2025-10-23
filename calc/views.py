from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Features
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def home(request):
    features = Features.objects.all()
    return render(request, 'index.html', {'features': features})

def result(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    res = num1 + num2
    return render(request, 'result.html', {'result': res})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('register')    
    else:
        return render(request, 'register.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    return render(request, 'login.html')    

def logout(request):
    auth.logout(request)
    return redirect('home')

def post_detail(request, pk):
    # post = Features.objects.get(id=pk)
    return render(request, 'post.html', {'pk': pk})