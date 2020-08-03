from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

def home(request):
    series_obj = series.objects.all()
    return render(request, "home.html", {"series_obj": series_obj})

def series_view(request):
    series_obj = series.objects.all()
    return render(request, "series.html", {"series_obj": series_obj})

def about(request):
    return render(request, "about.html")

def soulsearching(request):
    themodel = soulsearchingmodel.objects.all()
    return render(request, "series/soulsearching.html", {"themodel": themodel})

def thirtyonedaysofme(request):
    themodel = thirtyonedaysofmemodel.objects.all()
    return render(request, "series/thirtyonedaysofme.html", {"themodel": themodel})

def wanderlust(request):
    themodel = wanderlustmodel.objects.all()
    return render(request, "series/wanderlust.html", {"themodel": themodel})

def innerconscience(request):
    themodel = innerconsciencemodel.objects.all()
    return render(request, "series/innerconscience.html", {"themodel": themodel})

def regeneration(request):
    themodel = regenerationmodel.objects.all()
    return render(request, "series/regeneration.html", {"themodel": themodel})

def theuntoldtruth(request):
    themodel = theuntoldtruthmodel.objects.all()
    return render(request, "series/theuntoldtruth.html", {"themodel": themodel})

def thehumantrap(request):
    themodel = thehumantrapmodel.objects.all()
    return render(request, "series/thehumantrap.html", {"themodel": themodel})