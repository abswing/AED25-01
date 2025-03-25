class Cidade:

    def __init__(self, nome = "poa"):
        self.id = None
        self.nome = nome
    
    def __str__(self):
        return "id" + str(self.id) + " - nome da cidade " + self.nome


        