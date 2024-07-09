from django.shortcuts import render
from django.http import HttpResponse
def medecin(request):
   
    return render(request, 'diab/medecin.html')
