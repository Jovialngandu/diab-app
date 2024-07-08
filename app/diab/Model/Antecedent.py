from django.db import models
from diab.Model.Patient import Patient

class Antecedent(models.Model):
	patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
	allergy = models.JSONField(null=True)
	chronic_illness = models.JSONField(null=True) # maladie_chroniques
	genetic_illness = models.JSONField(null=True) # maladie_genetiques
	other = models.JSONField(null=True) # autres
	comments = models.JSONField(null=True) # commentaires

	class Meta:
		db_table = 'antecedents'
