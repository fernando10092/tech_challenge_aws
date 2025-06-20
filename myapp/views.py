from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .scrapers.scraper import getData
from .aws.upload import upload_file
import os

def View(request):
    return render(request, "index.html", {'message': 'Welcome to the Scraper App!'})

def Scraper(request):
    getData()
    return render(request, "index.html", {'message': 'Welcome to the Scraper App!'})

def Upload(request):
    if request.method == "POST":
        data = request.POST.get("inpName")
        bucket_name = os.getenv("AWS_BUCKET_NAME")
        file_path = f"C:/Users/Fernando/Desktop/Projetos/Tech_Challenge_AWS/data_extract/{data}.parquet"
        # file_path = f"C:/Users/Fernando/Desktop/Projetos/Tech_Challenge_AWS/{data}.xlsx"
        upload_file(file_path, bucket_name)
    
    return render(request, "index.html")
