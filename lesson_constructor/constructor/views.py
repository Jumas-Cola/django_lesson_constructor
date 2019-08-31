from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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


class MethodDetailView(generic.DetailView):
    model = TeachingMethod


@login_required
def my_methods(request, pk):
    if not (request.user) or (request.user.id != int(pk)):
        return HttpResponseRedirect(reverse_lazy('index'))
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
