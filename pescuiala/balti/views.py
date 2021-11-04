from django.db.models.functions.comparison import Coalesce
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg, Count, Value
from django.urls import reverse
from django.db.models.query_utils import Q

from .models import Balta, Judet
from .forms import ReviewForm, SortForm


def home(request):
    order = '?'
    if request.GET.getlist('option1'):
        if request.GET.getlist('option1')[0] == 'alfa_order_a_z':
            order = 'name'
        elif request.GET.getlist('option1')[0] == 'alfa_order_z_a':
            order = '-name'
        elif request.GET.getlist('option1')[0] == 'nota_sus':
            order = '-avg_reviews'
        elif request.GET.getlist('option1')[0] == 'nota_jos':
            order = 'avg_reviews'
    if request.GET.get('judete') is not None:
        checked_balti = [judet.id for judet in Judet.objects.all(
        ) if judet.name in request.GET.getlist('judete')]
    elif request.GET.get('scoate') == 'true':
        checked_balti = []
    else:
        checked_balti = [x for x in range(1, 43)]
    judete = Judet.objects.annotate(num_ap=Count(
        'balta__county')).filter(num_ap__gte=1)
    balti_list = Balta.objects.annotate(avg_reviews=Coalesce(
        Avg('recenzie__stars'), 0.0)).filter(county__in=checked_balti).order_by(order)
    if request.GET.get('search') is not None:
        balti_list = Balta.objects.filter(Q(name__icontains=request.GET.get(
            'search')) | Q(location__icontains=request.GET.get('search'))).order_by(order)
    choice_field = SortForm()
    return render(request, 'balti/home.html', {'balti_list': balti_list, 'judete': judete, 'checked_balti': checked_balti, 'choice_field': choice_field})


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
