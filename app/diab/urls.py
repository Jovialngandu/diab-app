from django.urls import path

from . import views


app_name = "diab"
urlpatterns = [
    path("", views.index, name="index"),
    path("logout", views.logout, name="logout"),
    path("login", views.login, name="login"),
    path("signin", views.signin, name="signin"),
    path("medecin", views.medecin, name="medecin"),
    path("patients", views.patients, name="patients"),
]