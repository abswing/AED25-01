from Cidade import Cidade

class Pessoa:
    def __init__(self, nome = None, cpf = None, cid = Cidade("Eldo") ):
        self.nome = None
        self.id = id
        self.cpf = cpf
        self.cidade = cid
        self.salario = 0.0
    
    def setSalario(self, valor):
        if valor > self.salario: 
            self.salario = valor

    def __str__(self):
        txt = "NOME: " +  self.nome
        txt += "\nCPF: " +  str(self.cpf)
        txt += "\nSalario: " +  str(self.salario)
        # txt += "\nCidade: "  + self.cidade.nome      
        txt += "\nCidade: " +  str(self.cidade)
        return txt
