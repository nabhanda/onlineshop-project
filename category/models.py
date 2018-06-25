from django.db import models

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title
