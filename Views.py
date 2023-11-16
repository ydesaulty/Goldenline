from django.shortcuts import render
from .models import Collecte
from django.http import HttpResponse
import csv

def graphique(request):
    collectes = Collecte.objects.all()
    context = {'collectes': collectes}
    return render(request, 'graphique.html', context)

def export(request):
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['categorie_socioprofessionnelle', 'categorie_depense', 'depense'])

    for collecte in Collecte.objects.all().values_list('categorie_socioprofessionnelle', 'categorie_depense', 'depense'):
        writer.writerow(collecte)

    response['Content-Disposition'] = 'attachment; filename="collecte.csv"'
    return response
