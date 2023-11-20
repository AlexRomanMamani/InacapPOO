import mysql.connector
from mysql.connector import errorcode

class Conexion:
    '''Clase para la conexion a la base de datos.'''
    def __init__(self):
        self.__host = "localhost"
        self.__port = "3306"
        self.__user = "root"
        self.__password = ""
        self.__database = "pokemondb"
        self.__mydb = None

    def getConexion(self):
        '''Este metodo se encarga de retornar la conexion a la base de datos.'''
        if self.__mydb is None: # Si no existe la conexion, se crea
            self.crearConexion()
        return self.__mydb
    
    def crearConexion(self):
        '''Este metodo se encarga de crear la conexión a la base de datos.'''
        try:
            self.__mydb = mysql.connector.connect( # Se crea la conexion
                host = self.__host, # Se pasan los parametros de la conexion
                port = self.__port, 
                user = self.__user,
                password = self.__password,
                database = self.__database
            )
            print("Conexion establecida")
        except mysql.connector.Error as err:
            # Se manejan los errores que pueden ocurrir
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR: # Si el error es por usuario o contraseña
                print("Usuario o contraseña incorrecto") 
            elif err.errno == errorcode.ER_BAD_DB_ERROR: # Si el error es por la base de datos
                print("No existe la base de datos")
            else:
                print(err)

# Laragorn habilita el puerto para conectar a la base de datos.