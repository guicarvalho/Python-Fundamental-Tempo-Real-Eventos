# coding:utf-8

salario = 500

def bonus_salario(salario):
    salario += 500
    print u'O bônus foi aplicado'
    return salario

print u'valor antes da bonificação => R$ %s' % salario
salario = bonus_salario(salario)
print u'valor após da bonificação => R$ %s' % salario
