import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage

def home(request):
    return render(request, 'pages/home.html')

def legal(request):
    return render(request, 'pages/legal.html')

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

def materiaux(request):
    return render(request, 'pages/materiaux.html')

def gallery(request):
    static_img_path = os.path.join(settings.BASE_DIR, 'pages', 'static', 'pages', 'images')
    subfolders = ['avant_apres', 'planche_ambiance', 'materiaux', 'rendu_3d']
    images = []
    for f in os.listdir(static_img_path):
        if f.lower().endswith(('.jpg')):
            images.append(f'pages/images/{f}')
    for folder in subfolders:
        folder_path = os.path.join(static_img_path, folder)
        if os.path.exists(folder_path):
            for f in os.listdir(folder_path):
                if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                    images.append(f'pages/images/{folder}/{f}')

    return render(request, 'pages/gallery.html', {'images': images})