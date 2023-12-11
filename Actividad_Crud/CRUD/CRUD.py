class CRUDUniversidad:
    ''' Clase que contiene los comandos DML.'''
    def __init__(self, cnx):
        if cnx is not None:
            self.__cnx = cnx # cnx es la conexion a la base de datos
    
    def listar_alumnos(self):
        ''' Este metodo lista asignaturas, nombres y apellidos de forma ascendente.'''
        sql = '''SELECT asignatura.nombreAsignatura ASIGNATURA, alumno.nombreAlumno NOMBRE, alumno.apellidoAlumno APELLIDO FROM alumno 
            JOIN notas ON alumno.codigoAlumno =  notas.codigoAlumno
            JOIN asignatura ON notas.codigoAsignatura = asignatura.codigoAsignatura
            ORDER BY asignatura.nombreAsignatura, alumno.nombreAlumno, alumno.apellidoAlumno  ASC; '''	# Se crea la consulta
        # Acento frances, es para que pokemon sea tratada como una tabla, y no un nombre reservado
        try:
            query_select = self.__cnx.cursor() # Cursor es un objeto que permite ejecutar las consultas
            query_select.execute(sql) # Se ejecuta la consulta
            myResult = query_select.fetchall() # myResult es una lista de tuplas
            #self.__cnx.close() # close() cierra la conexion 
            return myResult
        except Exception as ex:
            print("listar_alumnos -> {}".format(ex)) # Se manejan los errores que puedan ocurrir
            return False
    def listar_asignaturas_mayor_50_horas (self):
        ''' Listar las asignaturas cuya hora supere las 50'''
        sql = '''SELECT `asignatura`.`nombreAsignatura` ASIGNATURA, `asignatura`.`horasAsignatura` HORAS FROM `asignatura`
WHERE `asignatura`.`horasAsignatura` > 50'''
        try:
            query_select = self.__cnx.cursor() # Cursor es un objeto que permite ejecutar las consultas
            query_select.execute(sql) # Se ejecuta la consulta
            myResult = query_select.fetchall() # myResult es una lista de tuplas
            #self.__cnx.close() # close() cierra la conexion 
            return myResult
        except Exception as ex:
            print("listar_alumnos -> {}".format(ex)) # Se manejan los errores que puedan ocurrir
            return False
    def listar_alumnos_notas(selg):
        '''Listar a los alumnos cuya nota 1 estén entre 4.5 y 6.5 (ambas inclusive).'''
        sql = '''SELECT `alumno`.`nombreAlumno` NOMBRE, `notas`.`nota1` NOTA_1 FROM `alumno`
        JOIN `notas` ON `alumno`.`codigoAlumno` = `notas`.`codigoAlumno`
        WHERE `notas`.`nota1` >= 4.5 AND `notas`.`nota1` <= 6.5
        '''
        try:
            query_select = self.__cnx.cursor() # Cursor es un objeto que permite ejecutar las consultas
            query_select.execute(sql) # Se ejecuta la consulta
            myResult = query_select.fetchall() # myResult es una lista de tuplas
            #self.__cnx.close() # close() cierra la conexion 
            return myResult
        except Exception as ex:
            print("listar_alumnos -> {}".format(ex)) # Se manejan los errores que puedan ocurrir
            return False