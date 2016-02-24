from django.shortcuts import render
from . models import Service
from django.utils import timezone

# Create your views here.
def service_list(request):
    services = Service.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'scat/service_list.html', {'services':services})