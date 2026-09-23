from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.project_list, name='project_list'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    path('skills-certifications/', views.skill_certifications, name='skill_certifications'),
    path('contact/', views.contact, name='contact'),
]