from django.contrib import admin
from .models import *
# Register your models here.

class todoAdmin(admin.ModelAdmin):
    model = Todo
    list_display = ['title', 'description', ]

admin.site.register(Todo, todoAdmin)
