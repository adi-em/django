from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def job(request):
    return render(request, 'job_listing.html')

def blog(request):
    return render(request, 'blog.html')