# coding:utf-8


class ModaFoca(object):

    def __add__(self, n):
        return 1

    def __sub__(self, n):
        return 1


n = ModaFoca()

print n - 10 + n
