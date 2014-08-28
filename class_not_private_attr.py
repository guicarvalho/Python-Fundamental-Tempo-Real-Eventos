# coding:utf-8


class Dog(object):

    def __init__(self):
        self.idade = 2
        self._raca = 'Vira-lata'
        self.__nome = 'Rex'


rex = Dog()

print rex.idade
print rex._raca
print rex._Dog__nome


