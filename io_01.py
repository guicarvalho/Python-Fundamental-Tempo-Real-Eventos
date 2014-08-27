# coding: utf-8

'''
Usamos a função raw_input para ler valores do teclado,
a função retorna uma String, portanto devemos converter
para o tipo de dados desejado.
'''

nome = raw_input('Entre com o nome: ')
idade = int(raw_input('Entre com a idade: ')) # converte o valor da idade que entra como String para Inteiro

'''
Usamos a função print para exibir os valores das variáveis.
Repare que passamos uma String, e então usamos interpolação
para exibir os valores.
'''

print 'Nome: %s, Idade: %d' % (nome, idade)
