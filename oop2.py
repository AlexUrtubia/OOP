class Galleta: 
    def __init__(self, color, sabor):  
        #init agrega en las instancias las variables definidas 
        self.color = color
        self.sabor = sabor
    def imprimir_msje(self, valor):
        if valor > 2000:
            print("Las galletas estan muy caras")
        else:
            print("Messirbe")

galleta1 = Galleta("blanco","leche")
galleta2 = Galleta("café","chocolate")
galleta3 = Galleta("amarillo","vainilla")
print("Color:",galleta1.color)
print("Color:",galleta2.sabor)

class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = (int)(input("Ingrese el primer número"))
        self.num2 = (int)(input("Ingrese el segundo número"))
        self.sumar()
        self.restar()
        self.multiplicar()
        self.dividir()
    def sumar(self):
        suma = self.num1 + self.num2
        print("La suma es:",suma)
    def restar(self):
        resta = self.num1 - self.num2
        print("La resta es:",resta)
    def multiplicar(self):
        multi = self.num1 * self.num2
        print("La multiplicación es:",multi)
    def dividir(self):
        divid = self.num1 / self.num2
        print("La multiplicación es:",divid)
        