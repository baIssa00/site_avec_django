from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    prenom = models.CharField(max_length=150)
    nom = models.CharField(max_length=50)
    numero = models.CharField(max_length=100)
    email = models.EmailField (max_length=200)
    pub_date = models.DateTimeField('date published')
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    archive = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.prenom} {self.nom}"
