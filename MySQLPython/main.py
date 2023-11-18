from conexion.conexion import Conexion

try:
    cnx = Conexion()
    cnx.getConexion()
except Exception as ex:
    print("Main -> {}".format(ex))