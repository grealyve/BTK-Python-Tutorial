from django.db import models

# Create your models here.

class Horse(models.Model):
    chars = models.CharField(max_length=200)
    image = models.CharField(max_length=50, verbose_name="At resmi")

    def __str__(self):
        return self.chars
        