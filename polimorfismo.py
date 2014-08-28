# coding:utf-8


class Pessoa:
    def __init__(self, nome ='', idade=0):
        self.nome = nome
        self.idade = idade
                           
        def getIdade(self):
            return self.idade
    

class PessoaFisica(Pessoa):
    def __init__(self, CPF, nome='', idade=0):
        Pessoa.__init__(self, nome, idade)
        self.CPF = CPF
    

class PessoaJuridica(Pessoa):
    def __init__(self, CNPJ, nome='', idade=0):
        Pessoa.__init__(self, nome, idade)
        self.CNPJ = CNPJ
                                                                                            
a = Pessoa()
Pessoa.__init__(a, 'Leonardo', 22)
                                                                                             
b = PessoaFisica('122.333.332-1', nome='', idade=0)
banco = PessoaJuridica('00.000.000/0001-11', nome='Banco do Brasil', idade=435)
print a.nome   # imprime Leonardo
print a.idade  # imprime 22
print b.CPF    # imprime 122.333.332-1
print banco.CNPJ # imprime 00.000.000/0001-11
