from django.db import models
from diab.Model.Person import Person

class MedicalStaff(models.Model):
	person = models.OneToOneField(Person, on_delete = models.CASCADE, unique = True)
	fonction = models.CharField(max_length = 40)

	class Meta:
		db_table = 'medical_staffs'
