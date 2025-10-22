from django.shortcuts import render
from django.http import HttpResponse
from .models import Features

# Create your views here.

def home(request):
    features = Features.objects.all()
    return render(request, 'index.html', {'features': features})

def result(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    res = num1 + num2
    return render(request, 'result.html', {'result': res})