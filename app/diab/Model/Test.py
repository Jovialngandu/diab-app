from django.db import models
from diab.Model.Patient import Patient
from diab.Model.Medico import Medico
from diab.Model.Consultation import Consultation

class Test(models.Model):
	patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
	medico = models.ForeignKey(Medico, on_delete = models.CASCADE) # medecin
	consultation = models.ForeignKey(Consultation, on_delete = models.CASCADE)
	exam_type = models.CharField(max_length = 200) # type_examen
	exam_date = models.DateTimeField() # date_examen
	comments = models.JSONField(null=True) # comments

	class Meta:
		db_table = 'tests'
