from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .scrapers.scraper import getData

def View(request):
    return render(request, "index.html", {'message': 'Welcome to the Scraper App!'})

def Scraper(request):
    getData()
    return render(request, "index.html", {'message': 'Welcome to the Scraper App!'})

