from django.contrib import admin
from .models import Service
from .models import Person
from .models import Category
from .models import CategoryImage
from .models import Status
from .models import Provider
from .models import Support
from .models import Type

class CategoryImageInline(admin.TabularInline):
    model = CategoryImage


class CategoryAdmin(admin.ModelAdmin):
    inlines = [CategoryImageInline]

admin.site.register(Service)
admin.site.register(Person)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Status)
admin.site.register(Provider)
admin.site.register(Support)
admin.site.register(Type)



