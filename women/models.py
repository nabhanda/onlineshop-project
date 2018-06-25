from django.db import models

from category.models import Category


class Women(models.Model):
    class Meta:
        verbose_name_plural = 'Women'
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
