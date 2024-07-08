from django.db import models
from diab.Model.Person import Person

class Patient(models.Model):
	person = models.OneToOneField(Person, on_delete = models.CASCADE)
	diabetes_type = models.CharField(max_length = 60)
	feeding = models.JSONField(null=True) # alimentation
	diagnostic_date = models.DateTimeField()
	birth_date = models.DateField() # age
	remission_status = models.CharField(max_length = 1, choices=[
		('0', 'En rémission'),
		('1', 'Non en rémission'),
		('2', 'En évaluation')
	])

	class Meta:
		db_table = 'patients'
