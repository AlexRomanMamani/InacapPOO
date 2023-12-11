import time
class Comandos:
    def __init__(self, cnx):
        if cnx is not None:
            self.__cnx = cnx
    def selectUsuario(self, nick_usuario):
        '''Selecciona un usuario de la base de datos'''
        try:
            sql = 	""" SELECT * FROM `usuario` WHERE `nick_usuario` = %s; """
            val = (nick_usuario,)
            query = self.__cnx.cursor()
            query.execute(sql, val)
            return query.fetchall()
        except Exception as ex:
            print("seleccionarUsuario -> {}".format(ex))   
    def crearUsuario(self, nombre_usuario, apellido_usuario, nick_usuario, password_usuario, hash_password_usuario, codigo_acceso, activo_usuario):
        '''Crea un usuario en la base de datos'''
        try:
            sql = """ INSERT INTO `usuario` (`nombre_usuario`, `apellido_usuario`, `nick_usuario`, `password_usuario`, `hash_password_usuario`, `codigo_acceso`, `activo_usuario`) VALUES (%s, %s, %s, %s, %s, %s, %s); """
            val = (nombre_usuario, apellido_usuario, nick_usuario, password_usuario, hash_password_usuario, codigo_acceso, activo_usuario)
            query = self.__cnx.cursor()
            query.execute(sql, val)
            self.__cnx.commit()
            if query.lastrowid:
                print("Usuario creado con éxito")
        except Exception as ex:
            print("crearUsuario -> {}".format(ex))
    def listarUsuarios(self):
        '''Lista los usuarios de la base de datos'''
        try:
            sql = """ SELECT usuario.codigo_usuario, usuario.nombre_usuario, usuario.apellido_usuario, usuario.nick_usuario, acceso.nombre_acceso 
            FROM usuario
            INNER JOIN acceso ON usuario.codigo_acceso = acceso.codigo_acceso;
            """
            query = self.__cnx.cursor()
            query.execute(sql)
            return query.fetchall()
        except Exception as ex:
            print("listarUsuarios -> {}".format(ex))    
    def modificarUsuario(self, nombre_usuario, apellido_usuario, nick_usuario, password_usuario, hash_password_usuario, codigo):
        '''Modifica un usuario de la base de datos'''
        try:
            sql = 	""" UPDATE `usuario` SET `nombre_usuario` = %s,`apellido_usuario` = %s,`nick_usuario` = %s,`password_usuario` = %s,`hash_password_usuario` = %s WHERE `codigo_usuario` = %s; """
            val = (nombre_usuario, apellido_usuario, nick_usuario, password_usuario, hash_password_usuario, codigo)
            query = self.__cnx.cursor()
            query.execute(sql, val)
            self.__cnx.commit()
            if query.rowcount > 0:
                print("Usuario modificado correctamente")
        except Exception as ex:
            print("modificarUsuario -> {}".format)(ex)
    def eliminarUsuario(self, codigo):
        '''Elimina un usuario de la base de datos'''
        try:
            sql = 	""" DELETE FROM `usuario` WHERE `codigo_usuario` = %s; """
            val = (codigo,)
            query = self.__cnx.cursor()
            query.execute(sql, val)
            self.__cnx.commit()
            if query.rowcount > 0:
                print("Usuario eliminado correctamente")
        except Exception as ex:
            print("eliminarUsuario -> {}".format)(ex)
    def crearAsignatura(self, nombre_asignatura, horas_asignatura, activo_asignatura):
        '''Crea una asignatura en la base de datos'''
        try:
            sql = """ INSERT INTO `asignatura` (`nombre_asignatura`, `horas_asignatura`, `activo_asignatura`) VALUES (%s, %s, %s); """
            val = (nombre_asignatura, horas_asignatura, activo_asignatura)
            query = self.__cnx.cursor()
            query.execute(sql, val)
            self.__cnx.commit()
            if query.lastrowid:
                print("Asignatura creada con éxito")
        except Exception as ex:
            print("crearAsignatura -> {}".format(ex))
    def modificarAsignatura(self, nombre_asignatura, horas_asignatura, codigo):
        '''Modifica una asignatura de la base de datos'''
        try:
            sql = 	""" UPDATE `asignatura` SET `nombre_asignatura` = %s,`horas_asignatura` = %s WHERE `codigo_asignatura` = %s; """
            val = (nombre_asignatura, horas_asignatura, codigo)
            query = self.__cnx.cursor()
            query.execute(sql, val)
            self.__cnx.commit()
            if query.rowcount > 0:
                print("Asignatura modificada correctamente")
        except Exception as ex:
            print("modificarAsignatura -> {}".format)(ex)
    def eliminarAsignatura(self, codigo):
        '''Elimina una asignatura de la base de datos'''
        try:
            sql = 	""" DELETE FROM `asignatura` WHERE `codigo_asignatura` = %s; """
            val = (codigo,)
            query = self.__cnx.cursor()
            query.execute(sql, val)
            self.__cnx.commit()
            if query.rowcount > 0:
                print("Asignatura eliminada correctamente")
        except Exception as ex:
            print("eliminarAsignatura -> {}".format)(ex)
    def listarAsignaturas(self):
        '''Lista las asignaturas de la base de datos'''
        try:
            sql = """ SELECT asignatura.codigo_asignatura, asignatura.nombre_asignatura, asignatura.horas_asignatura FROM `asignatura`; """
            query = self.__cnx.cursor()
            query.execute(sql)
            return query.fetchall()
        except Exception as ex:
            print("listarAsignaturas -> {}".format(ex))
    def verificarDocente(self, codigo_usuario):
        '''Verifica si un usuario docente existe en la base de datos'''
        try:
            sql = """ SELECT * FROM `usuario` WHERE `codigo_usuario` = %s AND `codigo_acceso` = 2; """
            val = (codigo_usuario,)
            query = self.__cnx.cursor()
            query.execute(sql, val)
            if query.fetchall():
                return True
            else:
                return False
        except Exception as ex:
            print("verificarDocente -> {}".format(ex))
    def verificarAsignatura(self, codigo_asignatura):
        '''Verifica si una asignatura existe en la base de datos'''
        try:
            sql = """ SELECT * FROM `asignatura`WHERE `codigo_asignatura` = %s; """
            val = (codigo_asignatura,)
            query = self.__cnx.cursor()
            query.execute(sql, val)
            if query.fetchall():
                return True
            else:
                return False
        except Exception as ex:
            print("verificarAsignatura -> {}".format(ex))
    def crearDocenteAsignatura(self, codigo_usuario, codigo_asignatura):
        '''Asigna un docente a una asignatura en la base de datos'''
        try:
            sql = """ INSERT INTO `docente_asignatura` (`codigo_usuario`, `codigo_asignatura`) VALUES (%s, %s); """
            val = (codigo_usuario, codigo_asignatura)
            query = self.__cnx.cursor()
            query.execute(sql, val)
            self.__cnx.commit()
            if query.rowcount > 0:
                print("Docente asignado con éxito")
        except Exception as ex:
            print("crearDocenteAsignatura -> {}".format(ex))
    def listarDocentes(self):
        '''Lista los docentes de la base de datos'''
        try:
            sql = """ SELECT usuario.codigo_usuario, usuario.nombre_usuario, usuario.apellido_usuario FROM `usuario` WHERE `codigo_acceso` = 2; """
            query = self.__cnx.cursor()
            query.execute(sql)
            return query.fetchall()
        except Exception as ex:
            print("listarDocentes -> {}".format(ex))
    def modificarDocenteDeAsignatura(self, codigo_usuario, codigo_asignatura):
        '''Modifica un docente de una asignatura en la base de datos'''
        try:
            sql = """ UPDATE `docente_asignatura` SET `codigo_usuario` = %s WHERE `codigo_asignatura` = %s; """
            val = (codigo_usuario, codigo_asignatura)
            query = self.__cnx.cursor()
            query.execute(sql, val)
            self.__cnx.commit()
            if query.rowcount > 0:
                print("Docente modificado con éxito")
        except Exception as ex:
            print("modificarDocenteDeAsignatura -> {}".format)(ex)
    def listarAsignaturasConDocentes(self):
        '''Lista las asignaturas con sus respectivos docentes de la base de datos'''
        try:
            sql = """ SELECT asignatura.codigo_asignatura, asignatura.nombre_asignatura, usuario.nombre_usuario, usuario.apellido_usuario FROM `asignatura` 
            INNER JOIN docente_asignatura ON asignatura.codigo_asignatura = docente_asignatura.codigo_asignatura 
            INNER JOIN usuario ON docente_asignatura.codigo_usuario = usuario.codigo_usuario; """
            query = self.__cnx.cursor()
            query.execute(sql)
            return query.fetchall()
        except Exception as ex:
            print("listarAsignaturasConDocentes -> {}".format(ex))
    def listarDocentesDeUnaAsignatura(self, codigo_asignatura):
        '''Lista los docentes de una asignatura de la base de datos'''
        try:
            sql = """ SELECT usuario.codigo_usuario, usuario.nombre_usuario, usuario.apellido_usuario FROM `usuario` 
            INNER JOIN docente_asignatura ON usuario.codigo_usuario = docente_asignatura.codigo_usuario
            WHERE usuario.codigo_acceso = 2 AND docente_asignatura.codigo_asignatura = %s; """
            val = (codigo_asignatura,)
            query = self.__cnx.cursor()
            query.execute(sql, val)
            return query.fetchall()
        except Exception as ex:
            print("listarDocentesDeUnaAsignatura -> {}".format(ex))
    def eliminarDocenteAsignatura(self, codigo_usuario, codigo_asignatura):
        '''Elimina un docente de una asignatura de la base de datos'''
        try:
            sql = """ DELETE FROM `docente_asignatura` WHERE `codigo_usuario` = %s AND `codigo_asignatura` = %s; """ 
            val = (codigo_usuario, codigo_asignatura)
            query = self.__cnx.cursor()
            query.execute(sql, val)
            self.__cnx.commit()
            if query.rowcount > 0:
                print("Docente eliminado con éxito")
        except Exception as ex:
            print("eliminarDocenteAsignatura -> {}".format)(ex)
    def verificarAlumno(self, codigo_usuario):
        '''Verifica si un usuario alumno existe en la base de datos'''
        try:
            sql = """ SELECT * FROM `usuario` WHERE `codigo_usuario` = %s AND `codigo_acceso` = 3;"""
            val = (codigo_usuario,)
            query = self.__cnx.cursor()
            query.execute(sql, val)
            if query.fetchall():
                return True
            else:
                return False
        except Exception as ex:
            print("verificarAlumno -> {}".format(ex))
    def listarAlumnos(self):
        '''Lista los usuarios alumnos de la base de datos'''
        try:
            sql = """ SELECT * FROM `usuario` WHERE `codigo_acceso` = 3;"""
            query = self.__cnx.cursor()
            query.execute(sql)
            return query.fetchall()
        except Exception as ex:
            print("listarAlumnos -> {}".format(ex))
    def crearAlumnoAsignatura(self, codigo_usuario, codigo_asignatura):
        '''Asigna un usuario alumno a una asignatura en la base de datos'''
        try:
            sql = """ INSERT INTO `alumno_asignatura` (`codigo_usuario`, `codigo_asignatura`) VALUES (%s, %s);"""
            val = (codigo_usuario, codigo_asignatura)
            query = self.__cnx.cursor()
            query.execute(sql, val)
            self.__cnx.commit()
            if query.rowcount > 0:
                print("Alumno asignado con éxito")
        except Exception as ex:
            print("crearAlumnoAsignatura -> {}".format(ex))
    def listarAsignaturasConAlumnos(self):
        '''Lista las asignaturas con sus respectivos alumnos de la base de datos'''
        try:
            sql = """ SELECT asignatura.codigo_asignatura, asignatura.nombre_asignatura, usuario.nombre_usuario, usuario.apellido_usuario FROM `asignatura` 
            INNER JOIN alumno_asignatura ON asignatura.codigo_asignatura = alumno_asignatura.codigo_asignatura 
            INNER JOIN usuario ON alumno_asignatura.codigo_usuario = usuario.codigo_usuario; """
            query = self.__cnx.cursor()
            query.execute(sql)
            return query.fetchall()
        except Exception as ex:
            print("listarAsignaturasConAlumnos -> {}".format(ex))
    def modificarAlumnoDeAsignatura(self, codigo_usuario, codigo_asignatura):
        '''Modifica un alumno de una asignatura en la base de datos'''
        try:
            sql = """ UPDATE `alumno_asignatura` SET `codigo_usuario` = %s WHERE `codigo_asignatura` = %s; """
            val = (codigo_usuario, codigo_asignatura)
            query = self.__cnx.cursor()
            query.execute(sql, val)
            self.__cnx.commit()
            if query.rowcount > 0:
                print("Alumno modificado con éxito")
        except Exception as ex:
            print("modificarAlumnoDeAsignatura -> {}".format)(ex)
    def listarAlumnosDeUnaAsignatura(self, codigo_asignatura):
        '''Lista los alumnos de una asignatura de la base de datos'''
        try:
            sql = """ SELECT usuario.codigo_usuario, usuario.nombre_usuario, usuario.apellido_usuario FROM `usuario` 
            INNER JOIN alumno_asignatura ON usuario.codigo_usuario = alumno_asignatura.codigo_usuario
            WHERE usuario.codigo_acceso = 3 AND alumno_asignatura.codigo_asignatura = %s; """
            val = (codigo_asignatura,)
            query = self.__cnx.cursor()
            query.execute(sql, val)
            return query.fetchall()
        except Exception as ex:
            print("listarAlumnosDeUnaAsignatura -> {}".format(ex))
    def eliminarAlumnoAsignatura(self, codigo_usuario, codigo_asignatura):
        '''Elimina un alumno de una asignatura de la base de datos'''
        try:
            sql = """ DELETE FROM `alumno_asignatura` WHERE `codigo_usuario` = %s AND `codigo_asignatura` = %s; """
            val = (codigo_usuario, codigo_asignatura)
            query = self.__cnx.cursor()
            query.execute(sql, val)
            self.__cnx.commit()
            if query.rowcount > 0:
                print("Alumno eliminado con éxito")
        except Exception as ex:
            print("eliminarAlumnoAsignatura -> {}".format)(ex)
    def listarNotasAlumnoAsignatura(self, codigo_usuario, codigo_asignatura):
        '''Lista las notas de un alumno de una asignatura de la base de datos'''
        try:
            sql = """ SELECT alumno_asignatura.nota1, alumno_asignatura.nota2, alumno_asignatura.nota3 FROM `alumno_asignatura` 
            WHERE alumno_asignatura.codigo_usuario = %s AND alumno_asignatura.codigo_asignatura = %s; """
            val = (codigo_usuario, codigo_asignatura)
            query = self.__cnx.cursor()
            query.execute(sql, val)
            return query.fetchall()
        except Exception as ex:
            print("listarNotasAlumnoAsignatura -> {}".format(ex))
    def crearNota(self, nota1, nota2, nota3, codigo_usuario, codigo_asignatura):
        '''Crea notas de un alumno de una asignatura en la base de datos'''
        try:
            sql = """ UPDATE `alumno_asignatura` SET `nota1` = %s, `nota2` = %s, `nota3` = %s WHERE `codigo_usuario` = %s AND `codigo_asignatura` = %s; """
            val = (nota1, nota2, nota3, codigo_usuario, codigo_asignatura)
            query = self.__cnx.cursor()
            query.execute(sql, val)
            self.__cnx.commit()
            if query.rowcount > 0:
                print("Notas actualizadas con éxito")
        except Exception as ex:
            print("crearNota -> {}".format(ex))
    def eliminarNotasAlumnoAsignatura(self, codigo_usuario, codigo_asignatura):
        '''Elimina las notas de un alumno de una asignatura de la base de datos'''
        try:
            sql = """ UPDATE `alumno_asignatura` SET `nota1` = 0.0, `nota2` = 0.0, `nota3` = 0.0 WHERE `codigo_usuario` = %s AND `codigo_asignatura` = %s; """
            val = (codigo_usuario, codigo_asignatura)
            query = self.__cnx.cursor()
            query.execute(sql, val)
            self.__cnx.commit()
            if query.rowcount > 0:
                print("Notas eliminadas con éxito")
        except Exception as ex:
            print("eliminarNotasAlumnoAsignatura -> {}".format)(ex)
    def crearAsistencia(self, asistencia, codigo_usuario, codigo_asignatura ):
        '''Crea la asistencia de un alumno de una asignatura en la base de datos'''
        try:
            sql = """ UPDATE `alumno_asignatura` SET `asistencia` = %s WHERE `codigo_usuario` = %s AND `codigo_asignatura` = %s; """
            val = (asistencia, codigo_usuario, codigo_asignatura)
            query = self.__cnx.cursor()
            query.execute(sql, val)
            self.__cnx.commit()
            if query.rowcount > 0:
                print("Asistencia actualizada con éxito")
        except Exception as ex:
            print("crearAsistencia -> {}".format(ex))
    def listarAsistenciaAlumnoAsignatura(self, codigo_usuario, codigo_asignatura):
        '''Lista la asistencia de un alumno de una asignatura de la base de datos'''
        try:
            sql = """ SELECT alumno_asignatura.asistencia FROM `alumno_asignatura` 
            WHERE alumno_asignatura.codigo_usuario = %s AND alumno_asignatura.codigo_asignatura = %s; """
            val = (codigo_usuario, codigo_asignatura)
            query = self.__cnx.cursor()
            query.execute(sql, val)
            return query.fetchone()
        except Exception as ex:
            print("listarAsistenciaAlumnoAsignatura -> {}".format(ex))
    def eliminarAsistenciaAlumnoAsignatura(self, codigo_usuario, codigo_asignatura):
        '''Elimina la asistencia de un alumno de una asignatura de la base de datos'''
        try:
            sql = """ UPDATE `alumno_asignatura` SET `asistencia` = 0 WHERE `codigo_usuario` = %s AND `codigo_asignatura` = %s; """
            val = (codigo_usuario, codigo_asignatura)
            query = self.__cnx.cursor()
            query.execute(sql, val)
            self.__cnx.commit()
            if query.rowcount > 0:
                print("Asistencia eliminada con éxito")
        except Exception as ex:
            print("eliminarAsistenciaAlumnoAsignatura -> {}".format)(ex)
    def listarAsignaturasACargo(self, codigo_usuario):
        '''Lista las asignaturas a cargo de un docente de la base de datos'''
        try:
            sql = """ SELECT asignatura.codigo_asignatura, asignatura.nombre_asignatura FROM `asignatura` 
            INNER JOIN docente_asignatura ON asignatura.codigo_asignatura = docente_asignatura.codigo_asignatura 
            WHERE docente_asignatura.codigo_usuario = %s; """
            val = (codigo_usuario,)
            query = self.__cnx.cursor()
            query.execute(sql, val)
            return query.fetchall()
        except Exception as ex:
            print("listarAsignaturasACargo -> {}".format(ex))
    def listarAsignaturasDeAlumno(self, codigo_usuario):
        '''Lista las asignaturas de un alumno de la base de datos'''
        try:
            sql = """ SELECT asignatura.codigo_asignatura, asignatura.nombre_asignatura FROM `asignatura` 
            INNER JOIN alumno_asignatura ON asignatura.codigo_asignatura = alumno_asignatura.codigo_asignatura 
            WHERE alumno_asignatura.codigo_usuario = %s; """
            val = (codigo_usuario,)
            query = self.__cnx.cursor()
            query.execute(sql, val)
            return query.fetchall()
        except Exception as ex:
            print("listarAsignaturasDeAlumno -> {}".format(ex))