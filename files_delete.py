# coding:utf-8

# importamos o módulo os para ter acesso a função remove
import os

# utilizamos a função open para abrir um arquivo em Python
# o primeiro parâmetro é o nome do arquivo e o segundo é o modo de abertura
arq = open('meu_arq.txt', 'w')

os.remove(os.path.abspath('meu_arq.txt'))

print 'Arquivo excluído'
