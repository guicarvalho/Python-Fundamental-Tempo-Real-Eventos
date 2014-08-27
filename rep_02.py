# coding: utf-8

while True:
    i = int(raw_input('Entre com um número maior que 10 exibir olá na tela ou -1 para matar o processo: '))
    
    if i == -1:
        break
    elif i < 11:
        continue
    print 'valor => %d' % i
else:
    print 'O valor informado foi menor que 10'
