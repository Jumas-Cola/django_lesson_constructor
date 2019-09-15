from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.index, name='blog_index'),
    url(r'^articles/$', views.BlogArticleListView.as_view(), name='articles'),
    url(r'^articles/(?P<pk>\d+)$', views.BlogArticleDetailView.as_view(), name='article_detail'),
    url(r'^articles/(?P<pk>\d+)/comment$', views.BlogCommentCreate.as_view(), name='blogcomment_create'),
]
