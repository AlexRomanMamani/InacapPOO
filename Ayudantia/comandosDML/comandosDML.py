class ComnadosDML:
	def __init__(self, cnx):
		if cnx is not None:
			self.__cnx = cnx

	def seleccionarTodosAlumno(self):
		try:
			sql = 	"""
					SELECT * FROM `alumno`;
					"""
			query = self.__cnx.cursor()
			query.execute(sql)
			return query.fetchall()
		except Exception as ex:
			print("seleccionarTodosAlumno -> {}".format(ex))

	def seleccionarUnAlumno(self, codigo):
		try:
			sql = 	"""
					SELECT * FROM `alumno` WHERE `codigo` = %s;
					"""
			val = (codigo, )
			query = self.__cnx.cursor()
			query.execute(sql, val)
			return query.fetchall()
		except Exception as ex:
			print("seleccionarUnAlumno -> {}".format(ex))

	def ordenarDescendente(self):
		try:
			sql = 	"""
					SELECT * FROM `alumno` ORDER BY `apellido` DESC;
					"""
			query = self.__cnx.cursor()
			query.execute(sql)
			return query.fetchall()
		except Exception as ex:
			print("ordenarDescendente -> {}".format(ex))

	def rangoEdad(self):
		try:
			# sql = 	"""
			# 		SELECT * FROM `alumno` WHERE `edad` >= 15 and `edad` <= 25;
			# 		"""
			sql = 	"""
					SELECT * FROM `alumno` WHERE `edad` BETWEEN 15 and 25;
					"""
			query = self.__cnx.cursor()
			query.execute(sql)
			return query.fetchall()
		except Exception as ex:
			print("rangoEdad -> {}".format(ex))

	def apellidoPorInicial(self, letra_inicial):
		try:
			sql = 	"""
					SELECT * FROM `alumno` WHERE `apellido` LIKE %s;
					"""
			val = (letra_inicial + '%', )
			query = self.__cnx.cursor()
			query.execute(sql, val)
			return query.fetchall()
		except Exception as ex:
			print("apellidoPorInicial -> {}".format(ex))

	def apellidoPorFinal(self, letra_final):
		try:
			sql = 	"""
					SELECT * FROM `alumno` WHERE `apellido` LIKE %s;
					"""
			val = ('%' + letra_final, )
			query = self.__cnx.cursor()
			query.execute(sql, val)
			return query.fetchall()
		except Exception as ex:
			print("apellidoPorFinal -> {}".format(ex))

	def apellidoContenga(self, contenido):
		try:
			sql = 	"""
					SELECT * FROM `alumno` WHERE `apellido` LIKE %s;
					"""
			val = ('%' + contenido + '%', )
			query = self.__cnx.cursor()
			query.execute(sql, val)
			return query.fetchall()
		except Exception as ex:
			print("apellidoContenga -> {}".format(ex))

	def buscarPorCorreo(self, correo):
		try:
			sql = 	"""
					SELECT * FROM `alumno` WHERE `correo` = %s;
					"""
			val = (correo, )
			query = self.__cnx.cursor()
			query.execute(sql, val)
			return query.fetchall()
		except Exception as ex:
			print("buscarPorCorreo -> {}".format(ex))

	def alumnosActivos(self):
		try:
			sql = 	"""
					SELECT * FROM `alumno` WHERE `activo` = 1;
					"""
			query = self.__cnx.cursor()
			query.execute(sql)
			return query.fetchall()
		except Exception as ex:
			print("alumnosActivos -> {}".format(ex))

	def crearAlumno(self, nombre, apellido, edad, correo):
		try:
			sql = 	"""
					INSERT INTO `alumno`(`nombre`, `apellido`, `edad`, `correo`, `activo`)
					VALUES (%s,%s,%s,%s,1);
					"""
			val = (nombre, apellido, edad, correo)
			query = self.__cnx.cursor()
			query.execute(sql, val)
			self.__cnx.commit()
			if query.lastrowid:
				print("Alumno creado correctamente")
		except Exception as ex:
			print("crearAlumno -> {}".format)(ex)
	
	def modificarAlumno(self, nombre, apellido, edad, correo, codigo):
		try:
			sql = 	"""
					UPDATE `alumno` SET `nombre` = %s,`apellido` = %s,`edad` = %s,`correo` = %s WHERE `codigo` = %s;
					"""
			val = (nombre, apellido, edad, correo, codigo)
			query = self.__cnx.cursor()
			query.execute(sql, val)
			self.__cnx.commit()
			if query.rowcount > 0:
				print("Alumno modificado correctamente")
		except Exception as ex:
			print("modificarAlumno -> {}".format)(ex)

	def eliminarAlumno(self, codigo):
		try:

			sql = 	"""
					DELETE FROM `alumno` WHERE `codigo` = %s;
					"""
			val = (codigo, )
			query = self.__cnx.cursor()
			query.execute(sql, val)
			self.__cnx.commit()
			if query.rowcount > 0:
				print("Alumno eliminado correctamente")
		except Exception as ex:
			print("eliminarAlumno -> {}".format)(ex)
