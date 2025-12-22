from django.db import models
from django.contrib.auth.models import User  # Ak používaš vstavaný User model

class TODOO(models.Model):
    srno = models.AutoField(
        primary_key=True,  # Unikátny identifikátor pre každý záznam
        auto_created=True  # Automaticky vytvorený systémom
    )
    title = models.CharField(
        max_length=25  # Názov úlohy, max 25 znakov
    )
    date = models.DateTimeField(
        auto_now_add=True  # Dátum vytvorenia, nastaví sa automaticky
    )
    user = models.ForeignKey(
        User,  # Prepojenie na používateľa
        on_delete=models.CASCADE  # Ak sa používateľ vymaže, vymažú sa aj jeho úlohy
    )

    def __str__(self):
        return f"{self.title} (#{self.srno})"