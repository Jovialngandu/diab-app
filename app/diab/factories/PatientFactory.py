import factory
from faker import Faker

from diab.Model.Patient import Patient
# from diab.Model.Person import Person

from diab.factories.PersonFactory import PersonFactory

class PatientFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Patient

	__fake = Faker()

	person = factory.SubFactory(PersonFactory) # factory.Sequence(lambda n: PersonFactory.create()) # models.OneToOneField(Person, on_delete = models.CASCADE)
	
	diabetes_type = factory.LazyAttribute(lambda a: Faker().word()) # models.CharField(max_length = 60)
	feeding = factory.LazyAttribute(lambda a: Faker().json(data_columns={'nourriture' : 'word'}, num_rows=2)) # models.JSONField(null=True) # alimentation
	diagnostic_date = factory.LazyAttribute(lambda a: Faker().date_time_between(start_date = '-1y', end_date = 'now')) # models.DateTimeField()
	birth_date = factory.LazyAttribute(lambda a: Faker().date_of_birth()) # models.DateField() # age
	remission_status = factory.LazyAttribute(lambda a: Faker().word(ext_word_list = ['0', '1', '2'])) # models.CharField(max_length = 1, choices=[
	# 	('0', 'En rémission'),
	# 	('1', 'Non en rémission'),
	# 	('2', 'En évaluation')
	# ])
