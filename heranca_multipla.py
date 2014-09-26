# coding: utf-8

"""
Criando herança múltipla em Python.
"""

class Ave(object):
	__name = 'My Ave'
	
	def voar(self):
		print 'Voando, ',
		
	@property
	def name(self):
		return self.__name
		
		
class Fogo(object):
	__name = 'My Fogo'
	
	def pegar_fogo(self):
		print 'em chamas!'
	
	@property
	def name(self):
		return self.__name
		

class Fenix(Ave, Fogo):
	
	def __init__(self):
		super(Ave, self).__init__()
		super(Fogo, self).__init__()
		
		
	def voar(self):
		print u'Voando em chamas like a Fênix!'
		
	@property
	def name(self):
		return self.__name
		

f = Fenix()
f.voar()
f.pegar_fogo()
print f.name
