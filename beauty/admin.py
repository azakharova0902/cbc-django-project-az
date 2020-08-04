from django.contrib import admin

from .models import Service
from .models import Technician

@admin.register(Service)
class serviceAdmin(admin.ModelAdmin):
    # pass
    list_display = ['name', 'price', 'description', 'duration']

@admin.register(Technician)
class technicianAdmin(admin.ModelAdmin):
    list_display = ['name', 'expertise', 'story']