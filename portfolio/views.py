from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Project
from .forms import ContactForm

def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    return render(request, 'portfolio/about.html')

def projects(request):
    try:
        projects = Project.objects.all()
        return render(request, 'portfolio/projects.html', {'projects': projects})
    # except Exception as e:
    #     return render(request, 'portfolio/error.html', {'error': str(e)})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Here you can add code to handle the form data,
            # like sending an email or saving to database
            return render(request, 'portfolio/contact.html', {'form': form, 'success': True})
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio/project_detail.html', {'project': project})
