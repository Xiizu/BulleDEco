from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nom / Prénom")
    email = models.EmailField(verbose_name="Email")
    subject = models.CharField(max_length=150, verbose_name="Sujet")
    message = models.TextField(verbose_name="Message")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de réception")

    def __str__(self):
        return f"{self.subject} - {self.name}"

    class Meta:
        verbose_name = "Message de contact"
        verbose_name_plural = "Messages de contact"
        ordering = ['-created_at']
