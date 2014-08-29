# coding: utf-8

"""
Esse arquivo demonstra como lidar com exececoes
para abrir arquivos, fazer o uso do comando with.
São mostrados alguns comandos que usamos geralmente.
Podemos iterar os arquivos texto.
"""

try:
	with open('teste.txt', 'a') as file:
		print u'Arquivo aberto'
	print u'Arquivo fechado'
	
except IOError:
	print 'Erro ao abrir arquivo.'
	
meu_texto = 'Python assim como C++ e Smaltalk possui a tanto herança simples \
quando herança múltipla. \nNa herança simples, a classe extende de uma única \
super classe herdando todas as suas caracteristicas.\nDizemos que a classe \
filha é a classe mais especifica e a classe pai ou super classe é a classe \
mais genérica.\n'

try:
	with open('teste.txt', 'w') as file:
		file.writelines(meu_texto) # escrever um objeto iterável.
		print u'Escrita encerrada.'
	
	with open('teste.txt', 'r') as file:
		for line in file.readlines():
			print line
	
	print '-'*100
	# outro jeito para ler um única linhas de cada vez
	with open('teste.txt', 'r') as file:
		try:
			line = file.readline()
			while line:
				print line
				line = file.readline()
		except (IOError, Exception) as e:
			print 'Erro ao iterar file: ERRO: %s' % e
	
except Exception as e:
	print u'Erro ao abrir arquivo. ERRO: %s' % e.message
