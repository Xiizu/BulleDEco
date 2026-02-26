from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage

def home(request):
    return render(request, 'pages/home.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message_content = request.POST.get('message')
        try:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message_content
            )
            messages.success(request, "Votre message a été enregistré avec succès ! Je vous réponds très vite.")
        except Exception as e:
            messages.error(request, "Une erreur est survenue lors de l'envoi. Veuillez réessayer.")
        return redirect('contact')
    return render(request, 'pages/contact.html')

def admin_dashboard_redirect(request):
    return redirect('admin:pages_contactmessage_changelist')

def dabro(request):
    return render(request, 'pages/dabro.html')