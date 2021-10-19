from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.views import generic
from django.db.models import Avg
from django.urls import reverse

from .models import Balta
from .forms import ReviewForm


def home(request):
    balti_list = Balta.objects.annotate(avg_reviews=Avg('recenzie'))
    return render(request, 'balti/home.html', {'balti_list': balti_list})


def detail(request, balta_name):
    balta = get_object_or_404(Balta, name=balta_name)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.balta_id = balta.id
            form.save()
            return redirect(reverse('balti:detail', kwargs={'balta_name': balta.name}))
    else:
        form = ReviewForm()
        return render(request, 'balti/balta.html', {'balta': balta, 'form': form})
