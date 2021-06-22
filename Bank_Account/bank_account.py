#Crea una clase de BankAccount con los atributos tasa de interés y saldo
class BankAccount:
    def __init__(self, nombre, saldo=0, tasa_inte=0.01):
        self.nombre = nombre
        self.saldo = saldo
        self.tasa_inte = tasa_inte
        print("Saldo: ",self.saldo,"tasa interes: ",self.tasa_inte)
    #Agrega un método de depósito a la clase BankAccount   
    def deposit(self, amount):
        self.saldo =+ amount
        print(self.nombre,"a recibido un deposito de $",amount)
        return self
    #Agrega un método de retiro a la clase BankAccount
    def withdraw(self, amount):
        if self.saldo >= amount:
            self.saldo -= amount
            print(self.nombre,"a retirado $",amount,"de su cuenta")
        else:
            print("El saldo es insuficiente como para retirar $",amount,"\nIngrese un monto menor")
        return self
    #Agrega un método display_account_info a la clase BankAccount
    def display_account_info(self):
        print("Saldo en",self.nombre,": $",self.saldo)
        return self
    #Agrega un método yield_interest a la clase BankAccount
    def yield_interest(self):
        if self.saldo > 0:
            self.saldo += (self.tasa_inte*self.saldo)
            print(self.nombre,"a aumentado en $",self.saldo*self.tasa_inte,"su saldo gracias a intereses generados")
            return self

#Crea 2 cuentas
cta1=BankAccount("Cuenta 1",saldo=5000,tasa_inte=0.03)
cta2=BankAccount("Cuenta 2",150000,0.1)

#En la primera cuenta, realice 3 depósitos y 1 retiro, 
    #luego calcule los intereses y muestre la información de la cuenta en 
    # una sola línea de código (es decir, encadenamiento)
cta1.deposit(35000).deposit(43000).deposit(120000).withdraw(78990).yield_interest().display_account_info()
#En la segunda cuenta, realice 2 depósitos y 4 retiros, luego calcule los intereses y 
# muestre la información de la cuenta en una sola línea de código (es decir, encadenamiento)
cta2.deposit(160000).deposit(360000).withdraw(14400).withdraw(390000).withdraw(30000).withdraw(167000).yield_interest().display_account_info()