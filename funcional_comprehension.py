# coding:utf-8


'''
Em uma única linha podemos fazer todas as 
cartas de um baralho e ainda vincular o 
naípe as mesmas, por fim apenas ordenamos ela!!!
'''

print sorted([(naipe, num) for num in range(1,14) for naipe in ['O', 'P', 'E', 'C']])
