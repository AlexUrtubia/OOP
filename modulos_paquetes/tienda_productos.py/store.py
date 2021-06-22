import producto

class Store:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
    
    def agregar_productos(self, nuevo_producto):
        self.productos.append(nuevo_producto)
        return self
    
    def eliminar_producto (self, id):
        print("El producto",self.productos[id-1].nombre,"ha sido eliminado!")
        del self.productos[id-1]
        return self
    
    def inflacion (self, porcentaje):
        for producto in self.productos:
            producto.actualizar_precio(porcentaje, True)
        print("Todos los productos de",self.nombre,"han aumentado sus precios en un",porcentaje,"%")
        return self
    
    def actualizar_categoría (self, categoria, porcentaje):
        for producto in self.productos:
                if producto.categoria == categoria:
                    producto.actualizar_precio(porcentaje, False)
                    print()
        print("Los productos de la categoría",categoria,"han disminuido sus precios en un",porcentaje,"%")
        return self
    
    def info_productos(self):
        print("Lista de productos: ")
        for i in range (len(self.productos)):
            self.productos[i].print_info()
        return self

