# coding: utf-8

"""
Esse programa demostra uma excessao que
ocorre em tempo de execucao.
Remova o bloco try-except para visualizar
o erro.
"""

try:
	print u'Resultado da divisão: %d' % (1/0)
except ZeroDivisionError as e:
	print u'Não é possível dividir por zero. ERRO: %s' % e.message
	
"""
Poderiamos deixar o programa dinâmico com
o código abaixo.
"""
try:
	num = float(raw_input('Informe o valor a ser dividivo: '))
	div = float(raw_input('Informe o divisor: '))
	print u'Valor da operação: %.2f / %.2f = %.2f' % (num, div, (num/div))
except ZeroDivisionError as e:
	print u'Não é possível dividir por zero. ERRO: %s' % e.message
except ValueError as e:
	print u'Os valores informados não são válidos. ERRO: %s' % e.message
