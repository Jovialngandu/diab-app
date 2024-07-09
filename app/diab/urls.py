from django.urls import path

from . import views
from diab.view import index
from diab.view import profile
from diab.view import patients
from diab.view import dossier
from diab.view import historic_consult
from diab.view import login
from diab.view import medecin
from diab.view import signin
from diab.view import connexion


app_name = "diab"
urlpatterns = [
    path("", index.index, name="index"),

    path("login",login.login, name="login"),
    path("connexion",connexion.connexion, name="connexion"),

    path("signin",signin.signin, name="signin"),
    path("medecin",medecin.medecin, name="medecin"),
    path("patients", patients.patients, name="patients"),
    path("dossier",dossier.dossier, name="dossier"),
    path("profile", profile.profile, name="profile"),
    path("historic_consult",historic_consult.historic_consult, name="historic_consult"),
]