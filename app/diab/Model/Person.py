from django.db import models

class Person(models.Model):
	name = models.CharField(max_length = 40)
	firstname = models.CharField(max_length = 40)
	phone = models.JSONField(null=True)
	sex = models.CharField(max_length = 1, choices=[('f', 'Female'), ('m', 'Male')])
	address = models.CharField(max_length = 500)

	class Meta:
		db_table = 'people'
