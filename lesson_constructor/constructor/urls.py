from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('download/', views.download, name='download'),
    path('', views.index, name='index'),
    url(r'^method/create/$', views.MethodCreate.as_view(), name='method_create'),
    url(r'^method/(?P<pk>[-\w]+)/delete/$', views.MethodDelete.as_view(), name='method_delete'),
    url(r'^method/(?P<pk>[-\w]+)/update/$', views.MethodUpdate.as_view(), name='method_update'),
    url(r'^method/(?P<pk>[-\w]+)/copy/$', views.MethodCopy.as_view(), name='method_copy'),
    url(r'^method/(?P<id>[-\w]+)/comment/(?P<pk>\d+)/update/$', views.CommentUpdate.as_view(), name='comment_update'),
    url(r'^method/(?P<id>[-\w]+)/comment/(?P<pk>\d+)/delete/$', views.CommentDelete.as_view(), name='comment_delete'),
    url(r'^method/(?P<pk>[-\w]+)/comment/$', views.CommentCreate.as_view(), name='comment_create'),
    url(r'^method/(?P<pk>[-\w]+)$', views.MethodDetailView.as_view(), name='method_detail'),
    url(r'^id(?P<pk>\d+)$', views.my_methods, name='my_methods'),
]
