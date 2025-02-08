from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('about/', views.about, name='about'),  # About Me page
    path('projects/', views.projects, name='projects'),  # Featured Projects page
    path('contact/', views.contact, name='contact'),  # Contact page
]