from django.contrib import admin
from .models import BaseColor, ShadeColor, Palette

# Register your models here.

admin.site.register(BaseColor)
admin.site.register(ShadeColor)
admin.site.register(Palette)