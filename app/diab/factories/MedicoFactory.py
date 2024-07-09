import factory
from faker import Faker

from diab.Model.Medico import Medico
# from diab.Model.MedicalStaff import MedicalStaff

from diab.factories.MedicalStaffFactory import MedicalStaffFactory


class MedicoFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Medico

	__fake = Faker()

	medical_staff = factory.SubFactory(MedicalStaffFactory) # models.ForeignKey(MedicalStaff, on_delete = models.CASCADE)
