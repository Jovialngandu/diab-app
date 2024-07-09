from django.shortcuts import render
from django.http import HttpResponse
def dossier(request):
   
    return render(request, 'diab/dossier.html')
