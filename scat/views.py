from django.shortcuts import render,  get_object_or_404, redirect
from django.views.generic import ListView
from . models import Service
from . models import Category
from django.utils import timezone
from .forms import ServiceForm
from django.db.models import Q


def service_list(request):
    services = Service.objects.filter(published_date__lte=timezone.now()).order_by('title')
    return render(request, 'scat/service_list.html', {'services':services})
    
def category_list(request):
    cats = Category.objects.filter().order_by('category')
    return render(request, 'scat/category_list.html', {'cats':cats})
    
def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'scat/service_detail.html', {'service': service})

#services by category with type = Business	
def category_service(request, pk):
    catname = get_object_or_404(Category, pk=pk)
    services = Service.objects.filter(category=pk)
    return render(request, 'scat/category_service.html', {'services': services})
    

	
def service_new(request):
	if request.method == "POST":
			form = ServiceForm(request.POST)
			if form.is_valid():
				post = form.save(commit=False)
				post.author = request.user
				post.published_date = timezone.now()
				post.save()
				return redirect('service_detail', pk=post.pk)
	else:
		form = ServiceForm()
	return render(request, 'scat/service_edit.html', {'form': form})
	

	
