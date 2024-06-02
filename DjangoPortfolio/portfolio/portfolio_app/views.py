# portfolio_app/views.py
from django.shortcuts import render
from .models import Project

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'portfolio_app/project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'portfolio_app/project_detail.html', {'project': project})
