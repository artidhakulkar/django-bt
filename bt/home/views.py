from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):

    return render(request, "home/home.html")

def about(request):
    return render(request, "home/about.html")

def contact(request):
    return render(request, "home/contact.html")

def cources(request):
    return render(request, "home/cources.html")

def placement(request):
   return render(request, "home/placement.html")

def programming(request):
   return render(request, "home/programming.html")


def development(request):
   return render(request, "home/development.html")

def python_developer(request):
   return render(request, "home/python_developer.html")

def machine_learning(request):
   return render(request, "home/machine_learning.html")


def quantitive_aptitude(request):
   return render(request, "home/quantitive_aptitude.html")


def django(request):
   return render(request, "home/django.html")

def flask(request):
   return render(request, "home/flask.html")


def english_speaking(request):
   return render(request, "home/english_speaking.html")

def soft_skill(request):
   return render(request, "home/soft_skill.html")


def cad(request):
   return render(request, "home/cad.html")

