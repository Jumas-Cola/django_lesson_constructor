from django.shortcuts import render
from .models import BlogArticle
from .models import BlogComment
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic.list import MultipleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.contrib.auth.models import User
from .forms import SearchForm


def index(request):

    return render(
        request,
        'blog_index.html',
        context={},
    )


class BlogArticleListView(generic.ListView):
    model = BlogArticle
    form_class = SearchForm
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm()
        return context

    def get_queryset(self):
        form = self.form_class(self.request.GET)
        if form.is_valid():
            return BlogArticle.objects.filter(title__icontains=form.cleaned_data['query'])
        return BlogArticle.objects.all()


class BlogArticleDetailView(generic.DetailView, MultipleObjectMixin):
    model = BlogArticle

    def get_context_data(self, **kwargs):
        object_list = BlogComment.objects.filter(article=self.get_object())
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context


class BlogCommentCreate(LoginRequiredMixin, CreateView):
    model = BlogComment
    fields = ('text',)

    def get_success_url(self):
        return reverse_lazy('article_detail', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = get_object_or_404(
            BlogArticle, pk=self.kwargs['pk'])
        context['article_pk'] = self.kwargs['pk']
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.article = get_object_or_404(
            BlogArticle, pk=self.kwargs['pk'])
        return super().form_valid(form)


class BlogCommentDelete(LoginRequiredMixin, DeleteView):
    model = BlogComment

    def get_success_url(self):
        return self.request.GET['next']

    def get_object(self, queryset=None):
        obj = super().get_object()
        if not obj.author == self.request.user:
            raise Http404
        return obj


class BlogCommentUpdate(LoginRequiredMixin, UpdateView):
    model = BlogComment
    fields = ('text',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = get_object_or_404(
            BlogArticle, pk=self.kwargs['id'])
        context['article_pk'] = self.kwargs['id']
        return context

    def get_success_url(self):
        return self.request.GET['next']

    def get_object(self, queryset=None):
        obj = super().get_object()
        if not obj.author == self.request.user:
            raise Http404
        return obj

    def form_valid(self, form):
        form.instance.is_modified = True
        return super().form_valid(form)


# @login_required
def user_articles(request, pk):
    # if request.user.id != int(pk):
    #     raise Http404
    paginate_by = 5
    author = get_object_or_404(User, pk=pk)
    article_list = BlogArticle.objects.filter(
        author__id__exact=pk,
    )
    paginator = Paginator(article_list, paginate_by)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return render(
        request,
        'blog/user_articles.html',
        context={
            'is_paginated': True if len(article_list) > paginate_by else False,
            'page_obj': page_obj,
            'author': author,
            'form': SearchForm()
        },
    )
