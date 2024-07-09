import factory
from faker import Faker

from diab.Model.Antecedent import Antecedent
from diab.Model.Patient import Patient

# from diab.factories.PatientFactory import PatientFactory

class AntecedentFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Antecedent

	# __fake = Faker()

	patient = factory.LazyAttribute(lambda n: Patient.objects.order_by('?').first()) # models.ForeignKey(Patient, on_delete = models.CASCADE)
	
	allergy = factory.LazyAttribute(lambda a: Faker().word()) # models.JSONField(null=True)
	chronic_illness = factory.LazyAttribute(lambda a: Faker().words(nb=4)) # models.JSONField(null=True) # maladie_chroniques
	genetic_illness = factory.LazyAttribute(lambda a: Faker().words(nb=2)) # models.JSONField(null=True) # maladie_genetiques
	other = factory.LazyAttribute(lambda a: Faker().words(nb=3)) # models.JSONField(null=True) # autres
	comments = factory.LazyAttribute(lambda a: Faker().paragraphs(nb=5)) # models.JSONField(null=True) # commentaires
