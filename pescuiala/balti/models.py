from django.core import validators
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Judet(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Judet'
        verbose_name_plural = "Judete"


class Balta(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=150)
    county = models.ForeignKey(Judet, on_delete=models.CASCADE, blank=True)
    details = models.CharField(max_length=300)
    page = models.URLField(max_length=200, blank=True)
    map_page = models.URLField(max_length=200, blank=True)
    date_added = models.DateTimeField(
        verbose_name="Data adaugare", auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.location}"

    class Meta:
        verbose_name = "Balta"
        verbose_name_plural = "Balti"


class Recenzie(models.Model):
    stars = models.IntegerField(verbose_name="Nota", validators=[
                                MinValueValidator(1), MaxValueValidator(5)])
    title = models.CharField(verbose_name="Titlu", max_length=30)
    review = models.CharField(verbose_name="Recenzie", max_length=250)
    date_added = models.DateTimeField(
        verbose_name="Data adaugare", auto_now_add=True)
    balta = models.ForeignKey(Balta, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.stars} - {self.title}"

    class Meta:
        verbose_name = 'Recenzie'
        verbose_name_plural = 'Recenzii'
