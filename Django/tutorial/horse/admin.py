from django.contrib import admin
from .models import Horse

# Register your models here.

@admin.register(Horse)
class HorseAdmin(admin.ModelAdmin):
    list_display = ('chars',)
    list_display_links = ("chars",)
