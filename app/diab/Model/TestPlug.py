from django.db import models
from diab.Model.Test import Test
from diab.Model.Medico import Medico

class TestPlug(models.Model):
	test = models.ForeignKey(Test, on_delete = models.CASCADE)
	medico = models.ForeignKey(Medico, on_delete = models.CASCADE)

	class Meta:
		db_table = 'test_plugs'
