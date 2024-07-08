from django.urls import path

from . import views


app_name = "diab"
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("signin", views.signin, name="signin"),
    path("medecin", views.medecin, name="medecin"),
    path("patients", views.patients, name="patients"),
    path("dossier", views.dossier, name="dossier"),
    path("profile", views.profile, name="profile"),
    path("historic_consult", views.historic_consult, name="historic_consult"),
    
]