from django.db import models

class Profil(models.Model):
    image = models.ImageField(upload_to = 'image/')
