import factory
from faker import Faker

from diab.Model.MedicalStaff import MedicalStaff
# from diab.Model.Person import Person

from diab.factories.PersonFactory import PersonFactory


class MedicalStaffFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = MedicalStaff

	# __fake = Faker()

	person = factory.SubFactory(PersonFactory) # models.OneToOneField(Person, on_delete = models.CASCADE, unique = True)
	fonction = factory.LazyAttribute(lambda a: Faker().word()) # models.CharField(max_length = 40)
