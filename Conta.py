class Conta:

    logado = True
    tarifa = 1.99
    
    def __init__(self):
        self.__saldo = 0.0


    def getSaldo(self):
        if logado:
            return self.__saldo
        else: 
            return None

    def setSaldo(self, valor):
        if valor > self.__saldo:
            self.__saldo = valor
    
    def __descontarTarifa( self ):
        self.__saldo -= self.tarifa
    
    def sacar(self, valor):
        if self.__saldo >= valor + self.tarifa:
            self.__saldo -= valor 
            self.__descontarTarifa()
            print("saque realizado com sucesso")
            
    
    
    @Property
    def saldo(self):
        if logado:
            return self.__saldo
        else: 
            return None
        

    @saldo.setter
    def saldo(self, valor):
        if valor > self.__saldo:
            self.__saldo = valor 
