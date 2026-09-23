from django.shortcuts import render

from .models import Domain, Project, SkillGroup, Skill, Certification
from django.core.mail import send_mail
from .forms import ContactForm

def home(request):
    featured_projects = Project.objects.filter(featured=True)
    domains = Domain.objects.all()
    context = {
        'featured_projects': featured_projects, 
        'domains': domains,
    }
    return render(request, 'home.html', context)

def project_detail(request, slug):
    project = Project.objects.get(slug=slug)
    context = {
        'project': project,
    }
    return render(request, 'project_detail.html', context)

def project_list(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'project_list.html', context)

def skill_certifications(request):
    skill_groups = SkillGroup.objects.prefetch_related('skills').all()
    certifications = Certification.objects.all()
    context = {
        'skill_groups': skill_groups,
        'certifications': certifications,
    }
    return render(request, 'skill_certificate.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail(
                subject=f"New contact form submission from {name}",
                message=f'From: {name} ({email})\n\n{message}',
                from_email=email,
                recipient_list=['tandukarsupriya@gmail.com'],
            )
            return render(request, 'contact.html', {'form': ContactForm(), 'success': True})
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})