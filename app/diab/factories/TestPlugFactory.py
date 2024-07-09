import factory
from faker import Faker

from diab.Model.TestPlug import TestPlug
from diab.Model.Medico import Medico
from diab.Model.Test import Test

# from diab.factories.MedicoFactory import MedicoFactory
# from diab.factories.TestFactory import TestFactory

class TestPlugFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = TestPlug

	__fake = Faker()

	medico = factory.LazyAttribute(lambda n: Medico.objects.order_by('?').first()) # models.ForeignKey(Medico, on_delete = models.CASCADE)
	test = factory.LazyAttribute(lambda n: Test.objects.order_by('?').first()) # models.ForeignKey(Test, on_delete = models.CASCADE)
