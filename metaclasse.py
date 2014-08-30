# coding: utf-8

'''
testar

number = 1

number.__type__
number.__type__.__type__
'''

class Singleton(type):
	"""
	Metaclasse Singleton
	"""
	
	def __init__(cls, name, bases, dic):
		type.__init__(cls, name, bases, dic)
	
		# Retorna o próprio objeto na cópia
		def __copy__(self):
			return self
	
		# Retorna o próprio objeto na cópia recursiva
		def __deepcopy__(self, memo=None):
			return self
	
		cls.__copy__ = __copy__
		cls.__deepcopy__ = __deepcopy__
	
	def __call__(cls, *args, **kwargs):
		# Chamada que cria novos objetos,
		# aqui retorna sempre o mesmo
		try:
			return cls.__instanceMetaclasses
			# Se __instance não existir, então crie...
		except AttributeError:
			# A função super() pesquisa na MRO
			# a partir de Singleton
			cls.__instance = super(Singleton, cls).__call__(*args, **kwargs)
			return cls.__instance

import MySQLdb

class Con(object):
	"""
	Classe de conexão única
	"""
	
	# Define a metaclasse desta classe
	__metaclass__ = Singleton
	
	def __init__(self):
		# Cria uma conexão e um cursor
		con = MySQLdb.connect(user='root', passwd='root')
		self.db = con.cursor()
		# Sempre será usado o mesmo
		# objeto de cursor
	
class Log(object):
	"""
	Classe de log
	"""
	# Define a metaclasse desta classe
	
	__metaclass__ = Singleton
	
	def __init__(self):
		# Abre o arquivo de log para escrita
		self.log = file('msg.log', 'w')
		# Sempre será usado o mesmo
		# objeto de arquivo
	
	def write(self, msg):
		print msg
		# Acrescenta as mensagens no arquivo
		self.log.write(str(msg) + '\n')

# Conexão 1
con1 = Con()
Log().write('con1 id = %d' % id(con1))
con1.db.execute('show processlist')
Log().write(con1.db.fetchall())

# Conexão 2
con2 = Con()
Log().write('con2 id = %d' % id(con2))
con2.db.execute('show processlist')
Log().write(con2.db.fetchall())

import copy

# Conexão 3
con3 = copy.copy(con1)
Log().write('con3 id = %d' % id(con3))
con3.db.execute('show processlist')
Log().write(con2.db.fetchall())
