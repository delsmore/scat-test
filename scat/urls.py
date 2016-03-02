from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from . import views

urlpatterns = [
   # url(r'^$', views.service_list, name='service_list'),
    url(r'^$', views.category_list, name='category_list'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category_service, name='category_service'),
    url(r'^service/(?P<pk>[0-9]+)/$', views.service_detail, name='service_detail'),
	url(r'^service/new/$', views.service_new, name='service_new'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)