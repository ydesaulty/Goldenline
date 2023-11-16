from django.db import models

class Collecte(models.Model):
    categorie_socioprofessionnelle = models.CharField(max_length=200)
    categorie_depense = models.CharField(max_length=200)
    depense = models.FloatField()