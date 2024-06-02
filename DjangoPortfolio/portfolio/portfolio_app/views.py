from django.shortcuts import render
from .models import Project, Experience, Certification, Blog, Education

def home(request):
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    certifications = Certification.objects.all()
    educations = Education.objects.all()
    return render(request, 'home.html', {'projects': projects, 'experiences': experiences, 'certifications': certifications, 'educations': educations})

def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs.html', {'blogs': blogs})
