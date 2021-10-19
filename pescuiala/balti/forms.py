from django import forms
from .models import Recenzie


class ReviewForm(forms.ModelForm):
    # stars = forms.IntegerField(label="Nota", min_value=1, max_value=5)
    # title = forms.CharField(label="Titlu", max_length=50)
    # review = forms.CharField(label="Recenzie")

    class Meta:
        model = Recenzie
        fields = ['stars', 'title', 'review']


# class Recenzie(models.Model):
#     stars = models.IntegerField(default=1)
#     title = models.CharField(max_length=30)
#     review = models.CharField(max_length=250)
#     balta = models.ForeignKey(Balta, on_delete=models.CASCADE)
