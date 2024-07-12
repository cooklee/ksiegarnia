from django.db import models


class Skladnik(models.Model):
    name = models.CharField(max_length=123)

    def __str__(self):
        return self.name

class Przepis(models.Model):
    name = models.CharField(max_length=123)
    skladniki = models.ManyToManyField(Skladnik, through="SkladnikWPrzepisie")
    def __str__(self):
        return self.name


class SkladnikWPrzepisie(models.Model):
    przepis = models.ForeignKey(Przepis, on_delete=models.CASCADE)
    skladnik = models.ForeignKey(Skladnik, on_delete=models.CASCADE)
    jednostka = models.CharField(max_length=12)
    ilosc = models.IntegerField()

# Create your models here.
