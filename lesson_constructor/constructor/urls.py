from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.index, name='index'),
    url(r'method/(?P<pk>\d+)', views.MethodDetailView.as_view(), name='method_detail'),
    url(r'my_methods/(?P<pk>\d+)', views.my_methods, name='my_methods'),
]
