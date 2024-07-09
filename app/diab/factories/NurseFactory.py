import factory
from faker import Faker

from diab.Model.Nurse import Nurse
from diab.factories.MedicalStaffFactory import MedicalStaffFactory

# from diab.Model.MedicalStaff import MedicalStaff

class NurseFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Nurse

	__fake = Faker()

	medical_staff = factory.SubFactory(MedicalStaffFactory) # models.ForeignKey(MedicalStaff, on_delete = models.CASCADE)
