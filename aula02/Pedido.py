from Produto import  Produto
from Pessoa import  Pessoa
from datetime import date


class Pedido:

    def __init__(self, data = date.today(), cli = Pessoa("balcão") ):
        self.id = None
        self.data = data
        self.produto = []

    def addProd(self, prod ):
        if prod :
            self.Produtos.append( prod )
        soma = 0.0
        for p in self.Produtos:
            soma += p.preco
        return soma  

    def __str__(self):
        txt = "Data: " + str(self.data)
        txt += "\n" + str(self.cliente)
        txt += "\n produto: " 
        for p in self.produto:
            txt += "\nNome do produto: " + p.nome
            txt += "\nPreco:  " + str( p.preco )
            txt += "\n------------------------:"
        return txt 