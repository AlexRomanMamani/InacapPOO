import mysql.connector
from mysql.connector import errorcode

class Conexion:
    def __init__(self):
        self.__host = "localhost"
        self.__port = "3306"
        self.__user = "root"
        self.__password = ""
        self.__database = "pokemondb"
        self.__mydb = None

    def getConexion(self):
        if self.__mydb is None:
            self.crearConexion()
        return self.__mydb
    
    def crearConexion(self):
        try:
            self.__mydb = mysql.connector.connect(
                host = self.__host,
                port = self.__port,
                user = self.__user,
                password = self.__password,
                database = self.__database
            )
            print("Conexion establecida")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Usuario o contraseña incorrecto")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("No existe la base de datos")
            else:
                print(err)