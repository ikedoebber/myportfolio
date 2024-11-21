from django.shortcuts import render, HttpResponse
from home import models


def home(request):
    return render(request, 'home.html')


def project(request):
    return render(request, 'project.html')


from django.shortcuts import render
from .models import Contact


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Salvar no banco de dados
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()

        return render(request, 'contact.html', {'success': True})

    return render(request, 'contact.html')

