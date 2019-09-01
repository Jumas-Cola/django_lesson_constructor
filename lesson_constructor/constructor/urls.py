from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.index, name='index'),
    url(r'^method/create/', views.MethodCreate.as_view(), name='method_create'),
    url(r'^method/(?P<pk>[-\w]+)/delete/$', views.MethodDelete.as_view(), name='method_delete'),
    url(r'^method/(?P<pk>[-\w]+)/update/$', views.MethodUpdate.as_view(), name='method_update'),
    url(r'^method/(?P<pk>[-\w]+)', views.MethodDetailView.as_view(), name='method_detail'),
    url(r'^id(?P<pk>\d+)', views.my_methods, name='my_methods'),

]
