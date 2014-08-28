# coding:utf-8


class Dog(object):

    def __init__(self):
        self._nome = ''


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @nome.deleter
    def nome(self):
        del self._nome


rex = Dog()

rex.nome = 'rex'
print rex.nome
