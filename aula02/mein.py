from Cidade import Cidade
from Pessoa import Pessoa
from Produto import Produto
from Pedido import Pedido


c1 = Cidade()
C2 = Cidade("porto alegre")

p1 = Pessoa()
P2 = Pessoa("JOÃO", cid= c1 )

# print(  P2.cidade.nome )
print(P2)

prod01 = Produto()
prod02 = Produto("coca-cola", qtd= 100)
prod03 = Produto("pepsi", 8.99, 50)


ped01 = Pedido()
ped02 = Pedido( cli= P2)

ped02.addProd(prod03)
ped02.addProd(prod02)

print(ped02)