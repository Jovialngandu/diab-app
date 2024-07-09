import factory
from faker import Faker

from diab.Model.Test import Test
from diab.Model.Patient import Patient
from diab.Model.Medico import Medico
from diab.Model.Consultation import Consultation

# from diab.factories.PatientFactory import PatientFactory
# from diab.factories.MedicoFactory import MedicoFactory
# from diab.factories.ConsultationFactory import ConsultationFactory

class TestFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Test

	# __fake = Faker()

	patient = factory.LazyAttribute(lambda a: Patient.objects.order_by('?').first()) # models.ForeignKey(Patient, on_delete = models.CASCADE)
	medico = factory.LazyAttribute(lambda a: Medico.objects.order_by('?').first()) # models.ForeignKey(Medico, on_delete = models.CASCADE) # medecin
	consultation = factory.LazyAttribute(lambda a: Consultation.objects.order_by('?').first()) # models.ForeignKey(Consultation, on_delete = models.CASCADE)

	exam_type = factory.LazyAttribute(lambda a: Faker().word()) # models.CharField(max_length = 200) # type_examen
	exam_date = factory.LazyAttribute(lambda a: Faker().date_time_between(start_date = '-1y', end_date = 'now')) # models.DateTimeField() # date_examen
	comments = factory.LazyAttribute(lambda a: Faker().paragraphs(nb=4)) # models.JSONField(null=True) # comments
