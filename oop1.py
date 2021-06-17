# Creando la clase persona

# class Persona:
#     def iniciar(self, nombre):
#         self.name = nombre
#     def imprmir(self):
#         print("Nombre",self.name) # Hasta acá la clase persona tiene 2 métodos
# perso1 = Persona()
# perso1.iniciar("Pepito")
# perso1.imprimir()

# Crear la clase Alumno con sus atributos nombre y su nota
# Mostrar al final los valores de sus atributos y el estado del alumno (Apurba o Reprueba)

# class Alumno:
#     def __init__(self, nombre, nota):
#         self.nombre_=nombre
#         self.nota_=nota
        
#         # Definiendo una función para imprimir
#     def imprimir(self):
#         print("Nombre: ",self.nombre_)
#         print("Nota: ",self.nota_)
#     def mostrar_estado(self):
#         if self.nota_>=4:
#             print("Estado: Aprobado")
#         else:
#             print("Estado: Reprobado")

# alex = Alumno("Alex",6)
# sebastian = Alumno("Sebastian", 6)

# alex.imprimir()
# alex.mostrar_estado()

# sebastian.imprimir()
# sebastian.mostrar_estado()

#Definir la clase trabajador donde se solicite por 
#    pantalla el ingreso del nombre y el sueldo del trabajador
#    Luego, definir un método para imprimir el nombre y el sueldo
#    Defiir un método que dependiendo del sueldo aplique un bono
#    Si el sueldo es mayor a 500k no aplica el bono    
#        # Si el sueldo es menor a 500k eliga un bono del 15% del sueldo
#    Imprimir el sueldo total """

class Trabajador:
    def __init__(self):
        self.nombre=input("Ingrese su nombre ")
        self.sueldo=(int)(input("Ingrese su sueldo "))
        
        # Definiendo una función para imprimir
    def imprimir(self):
        print("Nombre: ",self.nombre)
        print("Sueldo: ",self.sueldo)
        
    def aplicar_bono(self):
        if self.sueldo < 500000:
            self.sueldo *= 1.15
            print("Aplica para bono")
        else:
            print("No aplica para bono")

trabajador1=Trabajador()
trabajador1.aplicar_bono()
trabajador1.imprimir()    
#juanito = Trabajador("Juan Tastico",490000)
#jose_antonio = Trabajador("José Antonio Unduriechaga Echeñique Luksic",8904600)
#karen = Trabajador("Karen Ulloa", 460000)
# lass Trabajador:
    
#     def __init__(self):
#         self.nombre = input("Ingrese su nombre:")
#         self.sueldo = (int)(input("Ingrese su sueldo:"))
    
#     def imprimir(self):
#         print("Nombre:", self.nombre)
#         print("Sueldo:", self.sueldo)
        
#     def aplicarBono(self):
#         if self.sueldo<500000:
#             self.sueldo = self.sueldo*1.15
#             print("Se aplicó el bono")
#         else:
#             print("No se aplicó el bono")
            
# trabajador1 = Trabajador()

# trabajador1.aplicarBono()

# trabajador1.imprimir()