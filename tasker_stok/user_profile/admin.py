from django.contrib import admin
from . import models

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('picture')

# Register your models here.
admin.site.register(models.Profile)