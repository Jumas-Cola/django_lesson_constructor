from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User


def main(request):
    return render(
        request,
        'main.html',
        context={},
    )


class UserDetailView(generic.DetailView):
    model = User
    template_name = 'user_detail.html'
