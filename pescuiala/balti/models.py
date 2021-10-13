from django.db import models


class Balta(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=150)
    coordinates = models.IntegerField()
    details = models.CharField(max_length=300)
    distance = models.FloatField()

    def __str__(self) -> str:
        return f"{self.name} - {self.location}"

    class Meta:
        verbose_name = "Balta"
        verbose_name_plural = "Balti"


class Recenzie(models.Model):
    stars = models.IntegerField(default=1)
    title = models.CharField(max_length=30)
    review = models.CharField(max_length=250)
    balta = models.ForeignKey(Balta, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.stars} - {self.title}"

    class Meta:
        verbose_name = 'Recenzie'
        verbose_name_plural = 'Recenzii'
