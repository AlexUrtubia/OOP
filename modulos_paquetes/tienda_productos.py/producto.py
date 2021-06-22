class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        
    def actualizar_precio(self, porcentaje, incrementado):
        if incrementado == True:
            self.precio += self.precio * porcentaje/100
        elif incrementado == False:
            self.precio -= self.precio * porcentaje/100
        else:
            print("Ingrese un valor booleano")
        return self
    
    def print_info (self):
        print("******************************")
        print("PRODUCTO".center(30))
        print("Nombre:",self.nombre)
        print("Precio:",self.precio)
        print("Categoría:",self.categoria)
        print("******************************")
        return self