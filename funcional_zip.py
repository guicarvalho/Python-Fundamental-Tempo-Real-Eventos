# coding:utf-8

# naípes das cartas
naipes = ['E', 'O', 'C', 'P'] * 13

# cria as 52 cartas do baralho
cartas = range(1, 14) * 4

# vincula cada carta a um naípe
baralho = zip(naipes, cartas)

# organiza as cartas do baralho
baralho.sort()

print baralho
print len(baralho)
