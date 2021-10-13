from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views import generic
from django.db.models import Avg

from .models import Balta


def home(request):
    balti_list = Balta.objects.annotate(avg_reviews=Avg('recenzie'))
    return render(request, 'balti/home.html', {'balti_list': balti_list})


def detail(request, balta_name):
    balta = get_object_or_404(Balta, name=balta_name)
    return render(request, 'balti/balta.html', {'balta': balta})
