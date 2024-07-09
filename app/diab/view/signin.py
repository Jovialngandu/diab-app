from django.shortcuts import render
from django.http import HttpResponse
def signin(request):
   
    return render(request, 'diab/register.html')
