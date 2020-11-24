from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView


def index(request):
    return render(request, 'html/main.html')
