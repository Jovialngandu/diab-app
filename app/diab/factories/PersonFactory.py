import factory
from faker import Faker

from diab.Model.Person import Person

class PersonFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Person

	# __fake = Faker()

	name = factory.LazyAttribute(lambda a: Faker().name())
	firstname = factory.LazyAttribute(lambda a: Faker().first_name())
	phone = factory.LazyAttribute(lambda a: [Faker().phone_number()])
	sex = factory.LazyAttribute(lambda a: Faker().word(ext_word_list = ['m', 'f']))
	address = factory.LazyAttribute(lambda a: Faker().profile(fields = 'mail').get('mail'))
