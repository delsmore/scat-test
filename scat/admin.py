from django.contrib import admin
from .models import Service
from .models import People
from .models import Category
from .models import Status
from .models import Provider
from .models import Support
from .models import Type
from .models import Portfolio
from .models import Location
from .models import Availability
    

class ServiceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name','guid','status']}),
        ('Definitions', {'fields': ['summary','description','logo'], 'classes': ['collapse']}),
        ('Category', {'fields': ['portfolio','category','type'], 'classes': ['collapse']}),
        ('Dependencies', {'fields': ['requires','required'], 'classes': ['collapse']}),
        ('Provider', {'fields': ['provider','service_owner','service_operations_manager'], 'classes': ['collapse']}),
        ('Support & Availability', {'fields': ['documentation','support','location','availability'], 'classes': ['collapse']}),
        (None,               {'fields': ['published']}),
    ]



admin.site.register(Service, ServiceAdmin)
admin.site.register(People)
admin.site.register(Category)
admin.site.register(Status)
admin.site.register(Provider)
admin.site.register(Support)
admin.site.register(Type)
admin.site.register(Portfolio)
admin.site.register(Location)
admin.site.register(Availability)








