from django.contrib import admin

from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    # Colonnes affichées dans la liste des messages
    list_display = ('name', 'subject', 'email', 'created_at')
    
    # Filtres sur le côté droit
    list_filter = ('subject', 'created_at')
    
    # Barre de recherche
    search_fields = ('name', 'email', 'message')
    
    # Rend les champs en lecture seule (pour éviter de modifier un message reçu par erreur)
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')