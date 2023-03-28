import csv  # Librería para abrir, leer y escribir archivos CSV


class Despensa:  # Clase Despensa

    def __init__(self): # Constructor de la clase Despensa
        pass # Inicializa el objeto de la clase Despensa

    def listarDespensa(self) -> bool: # Metodo para listar compras registradas
        try: # Prueba el codigo y si ocurre una Excepcion la atrapa
            with open("despensa.csv", "r") as file: # Abre el archivo para tener acceso a los registros
                reader = csv.DictReader(file, delimiter=",") # Crer un objeto reader para leer los registros separandolos por el delimitador ,
                for row in reader: # Recorre todos los registros encontrados y almacena temporalmente cada uno en row
                    print(f"Registro: {row}") # imprime los datos del registro como un diccionario
            return True # Regresa True si el metodo se ejecuto correctamente
        except Exception as e: # Atrapa cualquier excepcion
            print(f"Error listarProductos() :{e.args}") # Muestra en consola el error que ocurrio
            return False # Regresa False si ocurrio un error en el metodo

    def insertarDespensa(self, sku: str, nombre: str, unidad: str) -> bool: # Metodo para insertar despensa
        # TODO programar el método insertarDespensa()
        return False # Regresa False si ocurrio un error en el metodo

    def buscarDespensa(self, sku: str) -> bool: # Metodo para buscar una despensa
        # TODO programar el método buscarDespensa()
        return False # Regresa False si ocurrio un error en el metodo

    def borrarDespensa(self, sku: str) -> bool: # Metodo para borrar un producto
        # TODO programar el método borrarDespensa()
        return False # Regresa False si ocurrio un error en el metodo

    def actualizarDespensa(self, sku: str, nombre: str, unidad: str) -> bool: # Metodo para actualizar una despensa
        # TODO programar el método actualizarDespensa()
        return False # Regresa False si ocurrio un error en el metodo

despensa = Despensa() # Crea un objeto de la clase despensa
despensa.listarDespensa() # Llama al metodo listarDespensa()
