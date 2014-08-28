# coding:utf-8


# utilizamos a função open para abrir um arquivo em Python
# o primeiro parâmetro é o nome do arquivo e o segundo é o modo de abertura
arq = open('meu_arq.txt', 'r')

linhas = arq.readlines()

for linha in linhas:
    print linha
