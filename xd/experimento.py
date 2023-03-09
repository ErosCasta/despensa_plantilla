class Productos:

    def buscarProductos(self, sku:str, nombre:str , unidad:str) ->bool:
        print(f"Buscar: SKU:{sku} , Nombre:{nombre}, Unidad:{unidad}")
        return True

productos = Productos()

sku = input("SKU: ")
nombre = input("Nombre: ")
unidad = input("Unidad: ")
productos.buscarProductos(sku, nombre, unidad)
