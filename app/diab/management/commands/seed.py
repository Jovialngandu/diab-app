from django.core.management.base import BaseCommand
import factory as factory_boy
import time
import os
import warnings

# from diab.factories.PersonFactory import PersonFactory
from diab.factories.PatientFactory import PatientFactory
# from diab.factories.MedicalStaffFactory import MedicalStaffFactory
from diab.factories.MedicoFactory import MedicoFactory
from diab.factories.NurseFactory import NurseFactory
from diab.factories.AntecedentFactory import AntecedentFactory
from diab.factories.RemissionHistoryFactory import RemissionHistoryFactory
from diab.factories.ConsultationFactory import ConsultationFactory
from diab.factories.TestFactory import TestFactory
from diab.factories.TestPlugFactory import TestPlugFactory

class Command(BaseCommand):
	help = 'Exécution des Seeders'
	def createBatchCall(self, calls) :
		if isinstance(calls, list) :
			for call in calls :
				factory = call[0]
				nb_elmts = call[1]
				print(f'\n====== {factory.__name__}')
				if isinstance(factory, factory_boy.django.DjangoModelFactory.__class__) and isinstance(nb_elmts, int) and nb_elmts > 0:
					print('\n\n     Start...')
					start_at = time.time()
					try:
						warnings.simplefilter('ignore')
						factory.create_batch(nb_elmts)
						warnings.resetwarnings()
						pass
					except Exception as e:
						os.system('color')
						print('\033[31m\n\t' + str(e).replace("\n", "\n\t") + '\033[0m')
					end_at = time.time()
					print(f'\n     ...Finish : {round(end_at - start_at, 2)}s\n',)
				else :
					print('\n\n     Error : Les éléments dans `createBatchCall` ne sont pas conformes, "createBatchCall([[factory.django.DjangoModelFactory<class \'factory.base.FactoryMetaClass\'>, int > 0], ...])"')

	def handle(self, *args, **kwargs):
		self.createBatchCall([
			[PatientFactory, 50],
			[MedicoFactory, 20],
			[NurseFactory, 20],
			[AntecedentFactory, 20],
			[ConsultationFactory, 20],
			[TestFactory, 20],
			[TestPlugFactory, 20],
			[RemissionHistoryFactory, 20]
		])
