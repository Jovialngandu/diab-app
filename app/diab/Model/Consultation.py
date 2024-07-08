from django.db import models
from diab.Model.Patient import Patient
from diab.Model.Medico import Medico

class Consultation(models.Model):
	patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
	medico = models.ForeignKey(Medico, on_delete = models.CASCADE) # medecin

	comments = models.JSONField(null=True) # commentaires
	diagnostic = models.CharField(max_length = 500)
	
	treatment_plan = models.CharField(max_length = 500) # plan_traitement
	prescription = models.CharField(max_length = 500)

	class Meta:
		db_table = 'consultations'
