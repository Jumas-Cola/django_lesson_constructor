from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

import datetime
from .models import TeachingMethod, LessonPart


def index(request):
    author_name = 'admin'
    parts_with_items = {}
    lesson_parts = LessonPart.objects.all()
    for part in lesson_parts:
        parts_with_items[part] = TeachingMethod.objects.filter(
            author__username__exact=author_name,
            lesson_part__exact=part
        )

    return render(
        request,
        'index.html',
        context={
            'parts_with_items': parts_with_items,
            'lesson_parts': lesson_parts,
        },
    )


@login_required
def my_methods(request, pk):
    if request.user.id != int(pk):
        raise Http404
    parts_with_items = {}
    lesson_parts = LessonPart.objects.all()
    for part in lesson_parts:
        parts_with_items[part] = TeachingMethod.objects.filter(
            author__id__exact=pk,
            lesson_part__exact=part
        )

    return render(
        request,
        'constructor/my_methods.html',
        context={
            'parts_with_items': parts_with_items,
            'lesson_parts': lesson_parts,
        },
    )


class MethodDetailView(generic.DetailView):
    model = TeachingMethod
    template_name = 'constructor/method_detail.html'

    # def get_object(self, queryset=None):
    #     obj = super().get_object()
    #     if not obj.author == self.request.user:
    #         raise Http404
    #     return obj


class MethodDelete(LoginRequiredMixin, DeleteView):
    model = TeachingMethod
    template_name = 'constructor/method_confirm_delete.html'

    def get_success_url(self):
        return self.request.GET['next']

    def get_object(self, queryset=None):
        obj = super().get_object()
        if not obj.author == self.request.user:
            raise Http404
        return obj


class MethodUpdate(LoginRequiredMixin, UpdateView):
    model = TeachingMethod
    template_name = 'constructor/method_form.html'
    fields = ('title', 'description', 'lesson_part')

    def get_success_url(self):
        return self.request.GET['next']

    def get_object(self, queryset=None):
        obj = super().get_object()
        if not obj.author == self.request.user:
            raise Http404
        return obj


class MethodCreate(LoginRequiredMixin, CreateView):
    model = TeachingMethod
    template_name = 'constructor/method_form.html'
    fields = ('title', 'description', 'lesson_part')

    def get_success_url(self):
        return self.request.GET['next']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
