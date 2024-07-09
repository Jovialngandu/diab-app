from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignUpRequest(forms.Form):
    firstname = forms.CharField(max_length=100)
    name = forms.CharField()
    username = forms.CharField()
    password = forms.CharField()
    confirm_password = forms.CharField()
    fonction = forms.CharField()

    # def clean_field1(self):
    #     value = self.cleaned_data['field1']
    #     if len(value) < 5:
    #         raise forms.ValidationError('Le champ field1 doit contenir au moins 5 caractères.')
    #     return value

def signin(request):
    err_mess = request.session.get('error')
    if err_mess != None and err_mess.get('message') != None :
        err_mess = err_mess['message']
    request.session['error'] = None
    return render(request, 'diab/register.html', {"error_message" : err_mess})
def signup(request):
    if request.method == 'POST':
        validation = SignUpRequest(request.POST)
        if(validation.is_valid()) :
            if validation.cleaned_data['password'] == validation.cleaned_data['confirm_password'] :
                user = User.objects.create_user(username = validation.cleaned_data['username'], password = validation.cleaned_data['password'], first_name = validation.cleaned_data['firstname'], last_name = validation.cleaned_data['name'])
                user.save()
                return redirect('/diab/login')
            else :
                request.session['error'] = {'message' : 'La confirmation de mot de passe est différente du mot de passe !'}
                return redirect('/diab/signin')
        else :
            request.session['error'] = {'message' : 'Formulaire non conforme !'}
            return redirect('/diab/signin')
    else :
        return redirect('/diab/signin')
        # return HttpResponse('no')
