from django.db import models

# Create your models here.

class BaseColor(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class ShadeColor(models.Model):
    name = models.CharField(max_length=50)
    rgb = models.CharField(max_length=20)
    hex = models.CharField(max_length=10)
    base_color = models.ForeignKey(BaseColor, on_delete=models.CASCADE, related_name="shades")

    def __str__(self):
        return self.name

class Palette(models.Model):
    name = models.CharField(max_length=50)
    colors = models.ManyToManyField(ShadeColor)

    def __str__(self):
        return self.name