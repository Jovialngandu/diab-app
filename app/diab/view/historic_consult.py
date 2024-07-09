from django.shortcuts import render
from django.http import HttpResponse


def historic_consult(request):
   
    return render(request, 'diab/consultation_history.html')