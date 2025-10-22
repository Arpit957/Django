from django.shortcuts import render
from django.http import HttpResponse
from .models import Features

# Create your views here.

def home(request):
    feature1 = Features()
    feature1.id = 1 
    feature1.name = "Addition"
    feature1.description = "Perform addition of two numbers."

    feature2 = Features()
    feature2.id = 2
    feature2.name = "Subtraction"
    feature2.description = "Perform subtraction of two numbers."
    
    features = [feature1, feature2]
    return render(request, 'index.html', {'features': features})

def result(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    res = num1 + num2
    return render(request, 'result.html', {'result': res})