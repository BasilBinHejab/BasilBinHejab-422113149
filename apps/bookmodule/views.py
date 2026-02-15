from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'bookmodule/index.html')

def index2(request, val1=0):
    return HttpResponse(f'value1 = {val1}')
