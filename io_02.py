# coding: utf-8

'''
Para recuperar os parâmetros informados por linha de comando
vamos precisar do módulo sys das baterias inclusas do Python.
'''

import sys


lista_de_parametros = sys.argv # recuperando a lista de parametros

print 'Lista de argumentos => %s' % lista_de_parametros # exibindo a lista completa

print 'Pos => 0 da lista %s' % lista_de_parametros[0] # exibindo o primeiro valor da lista ... que é o nome do programa
