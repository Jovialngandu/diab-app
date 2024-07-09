from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate


def connexion(request):
    if request.method == 'POST':
        nameuser = request.POST.get('username')
        passwords = request.POST.get('password')

        user = authenticate(username = nameuser, password = passwords)

        if user is not None:
            return redirect('/diab')
        
        request.session['error']={ "message": "Nom d'utilisateur ou mot de passe incorrect"}
        return redirect('/diab/login')