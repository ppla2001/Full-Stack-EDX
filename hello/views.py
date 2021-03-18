from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request): #http request user made to enter our webpage
    return render(request, 'hello/index.html')

def pedro(request):
    return HttpResponse('Hello Pedro')

def david(request):
    return HttpResponse('Hello David')

def greet(request,name):
    return render(request, 'hello/greet.html', {
        'name': name.capitalize(),
    })