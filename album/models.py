from time import timezone
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Album(models.Model):
    title = models.CharField(max_length=250)
    created_date = models.DateTimeField(default=timezone.now, editable=False)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.ImageField(upload_to='media/', null=True, blank=True)

    def __str__(self) -> str:
        return f"titre : {self.title}"