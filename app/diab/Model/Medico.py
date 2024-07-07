from django.db import models
from diab.Model.MedicalStaff import MedicalStaff

class Medico(models.Model):
	medical_staff = models.ForeignKey(MedicalStaff, on_delete = models.CASCADE)

	class Meta:
		db_table = 'medicos'
