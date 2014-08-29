# coding:utf-8

def entrada_saida(f):
    def novo_f():
        print "Entrando em {0}".format(f.__name__)
        f()
        print "Saindo de {0}".format(f.__name__)
        return novo_f

@entrada_saida
def func1():
    print "Função 1"

@entrada_saida
def func2():
    print "Função 2"

if __name__ == '__main__':
    func1()
    func2()
