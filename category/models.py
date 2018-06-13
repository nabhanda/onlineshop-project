from django.db import models

class Category(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=30)
