from django.shortcuts import render,  get_object_or_404
from . models import Service
from django.utils import timezone

# Create your views here.
def service_list(request):
    services = Service.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'scat/service_list.html', {'services':services})
    
def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'scat/service_detail.html', {'service': service})