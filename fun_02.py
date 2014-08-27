# coding: utf-8

'''
A função show exibe o valor contido em args=>list
e kwargs=>dict. Ilustrando o poder dos parâmetros
em Python.
'''

def show(*args, **kwargs):
    print  args
    print  kwargs


show(0,1,2,3,4,5,6,7,8,9,10, nome='Guilherme', idade=20, altura=1.63)
