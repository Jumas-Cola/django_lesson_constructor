from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.index, name='blog_index'),
    url(r'^articles/$', views.BlogArticleListView.as_view(), name='articles'),
    url(r'^articles/(?P<pk>\d+)$', views.BlogArticleDetailView.as_view(), name='article_detail'),
    url(r'^articles/(?P<pk>\d+)/comment$', views.BlogCommentCreate.as_view(), name='blogcomment_create'),
    url(r'^articles/(?P<id>[-\w]+)/comment/(?P<pk>\d+)/update/$', views.BlogCommentUpdate.as_view(), name='blogcomment_update'),
    url(r'^articles/(?P<id>[-\w]+)/comment/(?P<pk>\d+)/delete/$', views.BlogCommentDelete.as_view(), name='blogcomment_delete'),
    url(r'^articles/id(?P<pk>\d+)$', views.user_articles, name='user_articles'),
]
