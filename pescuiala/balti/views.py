from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg, Count
from django.urls import reverse

from .models import Balta, Judet
from .forms import ReviewForm


def home(request):
    if 'csrfmiddlewaretoken' in request.GET:
        checked_balti = [int(id) for id in list(request.GET.keys())[1:]]
    else:
        checked_balti = [x for x in range(1, 43)]  # TO DO
    judete = Judet.objects.annotate(num_ap=Count(
        'balta__county')).filter(num_ap__gte=1)
    balti_list = Balta.objects.annotate(avg_reviews=Avg(
        'recenzie__stars')).filter(county__in=checked_balti)
    # if request.method == "POST":
    #     balti_list = Balta.objects.annotate(
    #         avg_reviews=Avg('recenzie__stars')).filter(county=17)
    #     return redirect(reverse('balti:home'))
    return render(request, 'balti/home.html', {'balti_list': balti_list, 'judete': judete, 'checked_balti': checked_balti})


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
        form = ReviewForm(label_suffix='')
    return render(request, 'balti/balta.html', {'balta': balta, 'form': form})


def about(request):
    return render(request, 'balti/about.html')


def contact(request):
    return render(request, 'balti/contact.html')
