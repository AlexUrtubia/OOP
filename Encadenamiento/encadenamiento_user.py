class User:		# aqui está lo que tenemos hasta ahora
    def __init__(self, name):
        self.name = name
        self.saldo = 0
    # agrega el método deposit 
    #def make_deposit(self, amount):	# toma un argumento que es el monto del depósito
    #    self.account_balance += amount	# la cuenta del usuario específico aumenta por la cantidad del valor recibido
    def make_deposit (self, amount):
        self.saldo += amount
        print(self.name,"a depositado $",amount,"a su cuenta")
        return self
    def make_withdrawal (self, amount):
        if self.saldo >= amount:
            self.saldo -= amount
            print(self.name,"a retirado $",amount,"de su cuenta")
        else:
            print("El saldo es insuficiente como para retirar $",amount,"\nIngrese un monto menor")
        return self
    def display_user_balance (self):
        print("Usuario: ",self.name)
        print("Saldo",self.name,": $",self.saldo)
        return self
    def transfer_money (self, other_user, amount):
        if self.saldo >= amount:
            self.saldo -= amount
            other_user.saldo += amount
            print(self.name,"ha transferido",amount,"a",other_user.name)
        else:
            print("El saldo es insuficiente")
        return self
        
user1=User("Victoria")
user2=User("Alex")
user3=User("Catalina")
# Haz que el primer usuario haga 3 depósitos y 1 retiro y luego muestre su saldo
user1.make_deposit(5000).make_deposit(15000).make_deposit(45000).display_user_balance()
# Haz que el segundo usuario haga 2 depósitos y 2 retiros y luego muestre su saldo
user2.make_deposit(350000).make_deposit(39700).make_withdrawal(290000).make_withdrawal(35000).display_user_balance()
# Haz que el tercer usuario haga 1 depósitos y 3 retiros y luego muestre su saldo
user3.make_deposit(15000).make_withdrawal(5000).make_withdrawal(5000).make_withdrawal(5000).make_withdrawal(5000).display_user_balance()
# BONIFICACIÓN: Agrega un método transfer_money; 
# haga que el primer usuario transfiera dinero al tercer usuario y 
# luego imprima los saldos de ambos usuarios
user1.transfer_money(user3,5000).display_user_balance()
user3.display_user_balance()