# coding:utf-8


def calcula(func, x, y):
    print 'Resultado: %s' % func(x, y)

def soma(x, y): return x+y
def sub(x, y): return x-y
def mul(x, y): return x*y
def div(x, y): return x/y

calcula(soma, 10, 2)
calcula(sub, 10, 2)
calcula(mul, 10, 2)
calcula(div, 10, 2)
