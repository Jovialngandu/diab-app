from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
   
    return render(request, "diab/index.html")

def login(request):
   
    return render(request, 'diab/login.html')

def logout(request):
   
    return render(request, 'diab/logout.html')

def signin(request):
   
    return render(request, 'diab/register.html')

def medecin(request):
   
    return render(request, 'diab/medecin.html')

def patients(request):
   
    return render(request, 'diab/patients.html')

def antecedant(request):
   
    return render(request, 'diab/medical_history.html')
def dossier(request):
   
    return render(request, 'diab/dossier.html')

def profile(request):
   
    return render(request, 'diab/profile.html')
def historic_consult(request):
   
    return render(request, 'diab/consultation_history.html')
def consult(request):
   
    return render(request, 'diab/consultation.html')