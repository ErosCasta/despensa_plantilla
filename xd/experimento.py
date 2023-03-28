import csv  # Librería para abrir, leer y escribir archivos CSV


class Productos:

    def buscarProducto(self) -> bool: # Metodo para buscar productos
        try: # Prueba el codigo y si ocurre una Excepcion la atrapa
            with open("productos.csv", "r") as file: # Abre el archivo para poder leer filas de informacion
                reader = csv.DictReader(file, delimiter=",") # Crer un objeto reader para leer los registros separandolos por el delimitador ,

                sku_buscar = input("Ingrese el SKU del producto que desea buscar: ") # Pide al usuario el SKU a buscar
                encontrado = False # Variable para indicar si se encontró el producto o no

                for row in reader: # Recorre todos los registros encontrados y almacena temporalmente cada uno en row
                    if row['sku'] == sku_buscar: # Compara el SKU buscado con el SKU de la fila actual
                        print(f"Registro encontrado: {row}") # Imprime la fila encontrada
                        encontrado = True # Marca el producto como encontrado
                        break # Termina el bucle ya que se encontró el producto

                if not encontrado: # If por si no exista el sku
                    print("Producto no encontrado") # Imprime el mensaje si el producto no se encontró

            return True # Retorna True si el método se ejecutó correctamente

        except Exception as e: # Atrapa cualquier excepcion
            print(f"Error buscarProducto(): {e.args}") # Muestra en consola el error que ocurrio
            return False  # Regresa False si ocurrio un error en el metodo

productos=Productos
productos.buscarProductos() # Llama al metodo buscarProductos()