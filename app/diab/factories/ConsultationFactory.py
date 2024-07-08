import factory
from faker import Faker

from diab.Model.Consultation import Consultation
from diab.Model.Patient import Patient
from diab.Model.Medico import Medico

# from diab.factories.PatientFactory import PatientFactory
# from diab.factories.MedicoFactory import MedicoFactory



class ConsultationFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Consultation

	# __fake = Faker()

	patient = factory.LazyAttribute(lambda a: Patient.objects.order_by('?').first()) # models.ForeignKey(Patient, on_delete = models.CASCADE)
	medico = factory.LazyAttribute(lambda a: Medico.objects.order_by('?').first()) # models.ForeignKey(Medico, on_delete = models.CASCADE) # medecin

	comments = factory.LazyAttribute(lambda a: Faker().paragraphs(nb=3)) # models.JSONField(null=True) # commentaires
	diagnostic = factory.LazyAttribute(lambda a: Faker().paragraph(nb_sentences = 2)) # models.CharField(max_length = 500)

	treatment_plan = factory.LazyAttribute(lambda a: Faker().paragraph(nb_sentences = 2)) # models.CharField(max_length = 500) # plan_traitement
	prescription = factory.LazyAttribute(lambda a: Faker().paragraph(nb_sentences = 2)) # models.CharField(max_length = 500)
