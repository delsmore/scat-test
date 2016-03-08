from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from . import views
from django.contrib import admin


urlpatterns = [
    url(r'^api/services/$', views.api_service_list, name='api_service_list'),
    url(r'^api/service/(?P<pk>[0-9]+)/$', views.api_service_detail, name='api_service_detail'),
    url(r'^api/people/$', views.api_people_list, name='api_people_list'),\
    url(r'^api/people/(?P<pk>[0-9]+)/$', views.api_people_detail, name='api_people_detail'),
    #url(r'^$', views.category_list, name='category_list'),
    url(r'^$', views.portfolio_list, name='portfolio_list'),
    url(r'^services/$', views.service_list, name='service_list'),
    url(r'^people/$', views.people_list, name='people_list'),
    #url(r'^category/(?P<pk>[0-9]+)/$', views.category_service, name='category_service'),
    url(r'^portfolio/(?P<pk>[0-9]+)/$', views.portfolio_service_list, name='portfolio_service_list'),
    url(r'^service/(?P<pk>[0-9]+)/$', views.service_detail, name='service_detail'),
    url(r'^people/(?P<pk>[0-9]+)/$', views.people_detail, name='people_detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.site_header = 'Service Catalogue Administration'