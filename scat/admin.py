from django.contrib import admin
from .models import Service
from .models import Category

admin.site.register(Service)
admin.site.register(Category)