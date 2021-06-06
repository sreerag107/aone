from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def usfun(request):
    return render(request, 'aoneuse.html')
