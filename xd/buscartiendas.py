import csv  # Librería para abrir, leer y escribir archivos CSV


class Tiendas:

    def buscarTiendas(self) -> bool: # Metodo para buscar tiendas
        try: # Prueba el codigo y si ocurre una Excepcion la atrapa
            with open("tiendas.csv", "r") as file: # Abre el archivo para poder leer filas de informacion
                reader = csv.DictReader(file, delimiter=",") # Crer un objeto reader para leer los registros separandolos por el delimitador ,

                id_buscar = input("Ingrese el id de la tienda que desea buscar: ") # Pide al usuario el id a buscar
                encontrado = False # Variable para indicar si se encontró la tienda o no

                for row in reader: # Recorre todos los registros encontrados y almacena temporalmente cada uno en row
                    if row['ID'] == id_buscar: # Compara el id buscando
                        print(f"Registro encontrado: {row}") # Imprime la fila encontrada
                        encontrado = True # Marca la tienda como encontrada
                        break # Termina el bucle ya que se encontró el producto

                if not encontrado: # If por si no exista el sku
                    print("Tienda no encontrada") # Imprime el mensaje si la tienda no se encontró

            return True # Retorna True si el método se ejecutó correctamente

        except Exception as e: # Atrapa cualquier excepcion
            print(f"Error buscarTienda(): {e.args}") # Muestra en consola el error que ocurrio
            return False  # Regresa False si ocurrio un error en el metodo

tiendas= Tiendas()
tiendas.buscarTiendas() # Llama al metodo buscarTiendas()