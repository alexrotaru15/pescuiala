from django import forms
from django.forms import widgets
from django.utils.translation import gettext_lazy as _
from .models import Recenzie


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Recenzie
        fields = ['stars', 'title', 'review']

        # labels = {
        #     'stars': _('writer')
        # }
        # help_texts = {
        #     'stars': _('nr de stele')
        # }
        error_messages = {
            'title': {
                'max_length': ('Puteti introduce maxim 30 de caractere.')
            },
            'stars': {
                'min_value': ('Introduceti o valoare intre 1 si 5'),
                'max_value': ('Introduceti o valoare intre 1 si 5')
            }
        }

        widgets = {
            'review': widgets.Textarea(attrs={
                'cols': 50,
                'rows': 5
            }),
        }


class SortForm(forms.Form):
    choices = [
        ('alfa_order_a_z', 'alfabetic a-z'),
        ('alfa_order_z_a', 'alfabetic z-a'),
        ('nota_sus', 'cea mai mare notă'),
        ('nota_jos', 'cea mai mică notă')
    ]
    option1 = forms.ChoiceField(choices=choices, label="Sortează")


# class Recenzie(models.Model):
#     stars = models.IntegerField(default=1)
#     title = models.CharField(max_length=30)
#     review = models.CharField(max_length=250)
#     balta = models.ForeignKey(Balta, on_delete=models.CASCADE)
