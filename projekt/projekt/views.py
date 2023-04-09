from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie, Director

def home(request):
    context = {
        'movies': Movie.objects.all(),
    }
    return render(request, 'home.html', context)

def reziseri(request):
    context = {
        'title' : "Režizéři",
        'directors': Director.objects.all(),
    }
    return render(request, 'reziseri.html', context)