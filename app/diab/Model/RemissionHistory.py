from django.db import models
from diab.Model.Patient import Patient
from diab.Model.Medico import Medico

class RemissionHistory(models.Model):
	patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
	medico = models.ForeignKey(Medico, on_delete = models.CASCADE) # medecin

	start_at = models.DateTimeField(null = True) # date_debut
	end_at = models.DateTimeField(null = True) # date_fin

	class Meta:
		db_table = 'remission_histories'
