from django.shortcuts import render
from .models import AboutMe, Skill, Education, Experience, Project, ContactInfo

def index(request):
    try:
        about_me = AboutMe.objects.first()  # Get the first AboutMe instance (should be only one)
    except AboutMe.DoesNotExist:
        about_me = None  # Handle the case where no AboutMe object exists

    skills = Skill.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    projects = Project.objects.all()

    try:
        contact_info = ContactInfo.objects.first() # Get the first ContactInfo object
    except ContactInfo.DoesNotExist:
        contact_info = None

    context = {
        'about_me': about_me,
        'skills': skills,
        'education': education,
        'experience': experience,
        'projects': projects,
        'contact_info': contact_info,
    }

    return render(request, 'website/index.html', context)

def about(request):
    try:
        about_me = AboutMe.objects.first()
    except AboutMe.DoesNotExist:
        about_me = None

    context = {'about_me': about_me}
    return render(request, 'website/about.html', context)

def contact(request):
    try:
        contact_info = ContactInfo.objects.first()
    except ContactInfo.DoesNotExist:
        contact_info = None

    context = {'contact_info': contact_info}
    return render(request, 'website/contact.html', context)

def projects(request):
    projects = Project.objects.all()  # Fetch all projects

    context = {'projects': projects}
    return render(request, 'website/projects.html', context)