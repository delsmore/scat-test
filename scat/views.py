from django.shortcuts import render,  get_object_or_404, redirect
from django.views.generic import ListView
from . models import Service
from . models import Category
from . models import People
from . models import Portfolio
from django.utils import timezone
from .forms import ServiceForm
from django.db.models import Q
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from scat.serializers import ServiceSerializer, PeopleSerializer


def service_list(request):
    services = Service.objects.filter().order_by('title')
    return render(request, 'scat/service_list.html', {'services':services})
    
def portfolio_list(request):
    portfolios = Portfolio.objects.filter().order_by('name')
    return render(request, 'scat/portfolio_list.html', {'portfolios':portfolios})
    
def category_list(request):
    cats = Category.objects.filter().order_by('name')
    return render(request, 'scat/category_list.html', {'cats':cats})
    
def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'scat/service_detail.html', {'service': service})
    
def people_detail(request, pk):
    people = get_object_or_404(People, pk=pk)
    services = Service.objects.filter(service_owner_id=pk)
    return render(request, 'scat/people_detail.html', {'people': people,'services': services})

#services by category with type = Business	
def category_service(request, pk):
    catname = get_object_or_404(Category, pk=pk)
    services = Service.objects.filter(category=pk, published=True,type=1)
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
	



class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
        

def api_service_list(request):
    """
    List all services
    
    """
    if request.method == 'GET':
        service = Service.objects.all()
        serializer = ServiceSerializer(service, many=True)
        return JSONResponse(serializer.data)

   
        

def api_service_detail(request, pk):
    """
    Retrieve a service.
    """
    try:
        service = Service.objects.get(pk=pk)
    except Service.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ServiceSerializer(service)
        return JSONResponse(serializer.data)
        
def api_people_list(request):
    """
    List all people
    """
    if request.method == 'GET':
        people = People.objects.all()
        serializer = PeopleSerializer(people, many=True)
        return JSONResponse(serializer.data)

   
        

def api_people_detail(request, pk):
    """
    Retrieve a person
    """
    try:
        people = People.objects.get(pk=pk)
    except People.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PeopleSerializer(people)
        return JSONResponse(serializer.data)


   

