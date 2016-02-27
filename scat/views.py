from django.shortcuts import render,  get_object_or_404, redirect
from django.views.generic import ListView
from . models import Service
from . models import Category
from django.utils import timezone
from .forms import ServiceForm

# Create your views here.
def service_list(request):
    services = Service.objects.filter(published_date__lte=timezone.now()).order_by('title')
    return render(request, 'scat/service_list.html', {'services':services})
    
def service_cats(request):
    cats = Category.objects.filter().order_by('category')
    return render(request, 'scat/service_cats.html', {'cats':cats})
    
def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'scat/service_detail.html', {'service': service})
    

	
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
	

	
