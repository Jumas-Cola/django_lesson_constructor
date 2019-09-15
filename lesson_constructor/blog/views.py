from django.shortcuts import render
from .models import BlogArticle
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin
from .models import BlogComment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import Http404


def index(request):

    return render(
        request,
        'blog_index.html',
        context={},
    )


class BlogArticleListView(generic.ListView):
    model = BlogArticle
    paginate_by = 5


class BlogArticleDetailView(generic.DetailView, MultipleObjectMixin):
    model = BlogArticle

    def get_context_data(self, **kwargs):
        object_list = BlogComment.objects.filter(method=self.get_object())
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context


class BlogCommentCreate(LoginRequiredMixin, CreateView):
    model = BlogComment
    fields = ('text',)

    def get_success_url(self):
        return reverse_lazy('method_detail', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['method'] = get_object_or_404(BlogArticle, pk=self.kwargs['pk'])
        context['method_pk'] = self.kwargs['pk']
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.method = get_object_or_404(BlogArticle, pk=self.kwargs['pk'])
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
        context['method'] = get_object_or_404(BlogArticle, pk=self.kwargs['id'])
        context['method_pk'] = self.kwargs['id']
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
