class ComandosDML:
    ''' Clase que contiene los comandos DML.'''
    def __init__(self, cnx):
        if cnx is not None:
            self.__cnx = cnx # cnx es la conexion a la base de datos
    
    def selectPokemon(self):
        '''Este metodo se encarga de realizar la consulta de los pokemones.'''
        sql ="SELECT * FROM `pokemon`;"	# Se crea la consulta
        # Acento frances, es para que pokemon sea tratada como una tabla, y no un nombre reservado
        try:
            query_select = self.__cnx.cursor() # Cursor es un objeto que permite ejecutar las consultas
            query_select.execute(sql) # Se ejecuta la consulta
            myResult = query_select.fetchall() # myResult es una lista de tuplas
            #self.__cnx.close() # close() cierra la conexion 
            return myResult
        except Exception as ex:
            print("selectPokemon -> {}".format(ex)) # Se manejan los errores que puedan ocurrir
            return False
