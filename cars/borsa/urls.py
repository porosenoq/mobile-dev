from django.conf.urls import url, include
from . import views
from borsa.views import CarDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.car_list, name='car_list'),
#    url(r'^(?P<pk>\d+)/(?P<slug>[\w\-]+)/$', CarDetailView.as_view(), name='car-detail'),
    url(r'^car/(?P<pk>\d+)/view/$', views.car_detail, name='car_detail'),
    url(r'^car/new/$', views.car_new, name='car_new'),
    url(r'^car/(?P<pk>\d+)/edit/$', views.car_edit, name='car_edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

