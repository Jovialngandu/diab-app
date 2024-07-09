import factory
from faker import Faker

from diab.Model.RemissionHistory import RemissionHistory
from diab.Model.Patient import Patient
from diab.Model.Medico import Medico

# from diab.factories.PatientFactory import PatientFactory
# from diab.factories.MedicoFactory import MedicoFactory

class RemissionHistoryFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = RemissionHistory

	# __fake = Faker()

	patient = factory.LazyAttribute(lambda a: Patient.objects.order_by('?').first()) # models.ForeignKey(Patient, on_delete = models.CASCADE)
	medico = factory.LazyAttribute(lambda a: Medico.objects.order_by('?').first()) # models.ForeignKey(Medico, on_delete = models.CASCADE) # medecin

	start_at = factory.LazyAttribute(lambda a: Faker().date_time_between(start_date = '-1y', end_date = '-2d')) # models.DateTimeField(null = True) # date_debut
	end_at = factory.LazyAttribute(lambda a: Faker().date_time_between(start_date = a.start_at, end_date = '+2d')) # models.DateTimeField(null = True) # date_fin
