# Se importan ambos códigos
import store as store
import producto as producto
# Se instancia una tienda bajo la clase Store
tienda1 = store.Store("Tienda de Alex")
# Se instancian 5 productos bajo la clase Producto con su respectivo nombre, precio y categoría
prod1 = producto.Producto("Agua mineral", 900,"Bebidas")
prod2 = producto.Producto("Pan", 1000,"Panadería")
prod3 = producto.Producto("Queso", 2700,"Lacteos")
prod4 = producto.Producto("Tallarines",890,"Abarrotes")
prod5 = producto.Producto("Salsa de tomate", 490,"Abarrotes")
# Se agregan a a tienda los 5 productos creados
tienda1.agregar_productos(prod1).agregar_productos(prod2).agregar_productos(prod3).agregar_productos(prod4).agregar_productos(prod5)
# Se eliminan 2 productos de la tienda 
# El producto 2 es el pan
tienda1.eliminar_producto(2)
# Al eliminar un producto, la lista se actualiza, por lo que 
# el producto que antes estaba en la posición 1, ya no existe y se sustituye por el que le sigue
# EL producto 2 ahora es el queso
tienda1.eliminar_producto(2)
# Se despliega la info de los productos existentes
tienda1.info_productos()
# Todos los productos de la tienda aumentan sus precios un 10% con el método inflación 
# y nuevamente se despliegan los detalles de cada producto
tienda1.inflacion(10).info_productos()
# Se reducen los precios de la categoría Abarrotes en un 20% y se despliega la lista actualizada
tienda1.actualizar_categoría("Abarrotes",20).info_productos()