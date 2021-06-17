class Cliente:
    def __init__(self,name):
        self.name = name
        self.monto = 0
    def depositar (self, monto):
        self.monto += monto
    def giro(self, monto):
        self.monto -= monto
    def devolver_monto(self):
        return self.monto
    def print_saldo(self):
        print(self.name,"Usted tiene un saldo de:",self.monto)

class Banco:
    def __init__(self):
        self.cliente1 = Cliente("Juanito")
        self.cliente2 = Cliente("Pepito")
    def realizar_tranza(self):
        self.cliente1.depositar(1000)
        self.cliente2.depositar(10000)
        self.cliente1.giro(500)
        self.cliente2.giro(50000)
    def imprimir_resultado(self):
        self.cliente1.print_saldo()
        self.cliente2.print_saldo()

bco=Banco()
bco.realizar_tranza()
bco.imprimir_resultado()