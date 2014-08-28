# coding:utf-8


class MyObject(object):

    # Aqui colocamos nossos parâmetros
    my_vars = []

    # Método que inicializa a classe
    def __init__(self, vars_list=None):
        print '__init__'

    # Método que destrói a classe
    def __done__(self):
        print '__done__'

    # Método de objeto
    def objeto(self):
        print 'método de objeto'

    # Método de classe
    def classe(cls, args):
        print 'método de classe'
    
    # Método estático
    def estatico(args):
        print 'Método estático'


