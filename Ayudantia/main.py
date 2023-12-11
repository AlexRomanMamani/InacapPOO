from conexion.conexion import Conexion
from comandosDML.comandosDML import ComnadosDML

try:
	lista_menu = [
				"Crear alumno",
				"Modificar datos del alumno",
				"Eliminar alumno",
				"Listar todos los alumnos",
				"Ordenar los alumnos de forma descendente por apellido",
				"Listar a todos los alumnos cuya edad este entre el 15 y 25",
				"Listar a todos los alumnos cuyo apellido comiencen con la letra indicada por el usuario",
				"Listar a todos los alumnos cuyo nombre termine con la letra indicada por el usuario",
				"Listar a todos los alumnos cuyo apellido contenga una letra o letras indicada por el usuario",
				"Buscar un alumno por su correo",
				"Listar a todos los alumnos activos en el sistema (activo = 1)"
				]
	cnx = Conexion()
	DML = ComnadosDML(cnx.getConexion())
		
	while True:
		print("Menú:")
		for i in range(len(lista_menu)):
			print("{}- {}".format(i +1, lista_menu[i]))
		print("0- Salir")
		opcion = int(input("Ingrese una opción: "))

		if opcion == 1:
			print("Crear alumno:")
			print("-" * 30)

			nombre = input("Ingrese el nombre del alumno: ")
			apellido = input("Ingrese el apellido del alumno: ")
			edad = int(input("Ingrese el edad del alumno: "))
			correo = input("Ingrese el correo del alumno: ")
			
			DML.crearAlumno(nombre, apellido, edad, correo)

		elif opcion == 2:
			print("Modificar alumno:")
			print("-" * 30)

			codigo = int(input("Ingrese el código del alumno: "))
			nombre = input("Ingrese el nombre del alumno: ")
			apellido = input("Ingrese el apellido del alumno: ")
			edad = int(input("Ingrese el edad del alumno: "))
			correo = input("Ingrese el correo del alumno: ")
			
			DML.modificarAlumno(nombre, apellido, edad, correo, codigo)

		elif opcion == 3:
			print("Eliminar alumno:")
			print("-" * 30)

			continuar = False

			codigo = int(input("Ingrese el código del alumno: "))

			if DML.seleccionarUnAlumno(codigo):
				for alumno in DML.seleccionarUnAlumno(codigo):
					continuar = True if input("¿Esta seguro que quiere eliminar al alumno {} {}?: ".format(alumno[1], alumno[2])).upper() == 'S' else False
					if continuar:
						DML.eliminarAlumno(codigo)
			else:
				print("No se econtraron registros")


			print("")
		elif opcion == 4:
			print("Listado de todos los alumnos:")
			print("-" * 30)

			if len(DML.seleccionarTodosAlumno()):
				for alumno in DML.seleccionarTodosAlumno():
					print("[{}] {} {} ({}): {} ({})".format(alumno[0], alumno[1], alumno[2], alumno[3], alumno[4], alumno[5]))
			else:
				print("No se encontraron registros")
		elif opcion == 5:
			print("Orden descendente:")
			print("-" * 30)

			if len(DML.ordenarDescendente()):
				for alumno in DML.ordenarDescendente():
					print("[{}] {} {} ({}): {} ({})".format(alumno[0], alumno[1], alumno[2], alumno[3], alumno[4], alumno[5]))
			else:
				print("No se encontraron registros")
		elif opcion == 6:
			print("Rango edad:")
			print("-" * 30)

			if len(DML.rangoEdad()):
				for alumno in DML.rangoEdad():
					print("[{}] {} {} ({}): {} ({})".format(alumno[0], alumno[1], alumno[2], alumno[3], alumno[4], alumno[5]))
			else:
				print("No se encontraron registros")
		elif opcion == 7:
			print("Apellido por inicial:")
			print("-" * 30)

			letra_inicial = input("Ingrese la letra inicial del apellido: ")

			if len(DML.apellidoPorInicial(letra_inicial)):
				for alumno in DML.apellidoPorInicial(letra_inicial):
					print("[{}] {} {} ({}): {} ({})".format(alumno[0], alumno[1], alumno[2], alumno[3], alumno[4], alumno[5]))
			else:
				print("No se encontraron registros")
		elif opcion == 8:
			print("Apellido por final:")
			print("-" * 30)

			letra_final = input("Ingrese la letra final del apellido: ")

			if len(DML.apellidoPorFinal(letra_final)):
				for alumno in DML.apellidoPorFinal(letra_final):
					print("[{}] {} {} ({}): {} ({})".format(alumno[0], alumno[1], alumno[2], alumno[3], alumno[4], alumno[5]))
			else:
				print("No se encontraron registros")
		elif opcion == 9:
			print("Apellido que contiene:")
			print("-" * 30)

			contenido = input("Ingrese el contenido del apellido: ")

			if len(DML.apellidoContenga(contenido)):
				for alumno in DML.apellidoContenga(contenido):
					print("[{}] {} {} ({}): {} ({})".format(alumno[0], alumno[1], alumno[2], alumno[3], alumno[4], alumno[5]))
			else:
				print("No se encontraron registros")
		elif opcion == 10:
			print("Alumo por correo:")
			print("-" * 30)

			correo = input("Ingrese el correo del alumno a buscar: ")

			if len(DML.buscarPorCorreo(correo)):
				for alumno in DML.buscarPorCorreo(correo):
					print("[{}] {} {} ({}): {} ({})".format(alumno[0], alumno[1], alumno[2], alumno[3], alumno[4], alumno[5]))
			else:
				print("No se encontraron registros")
		elif opcion == 11:
			print("Alumos activos:")
			print("-" * 30)

			if len(DML.alumnosActivos()):
				for alumno in DML.alumnosActivos():
					print("[{}] {} {} ({}): {} ({})".format(alumno[0], alumno[1], alumno[2], alumno[3], alumno[4], alumno[5]))
			else:
				print("No se encontraron registros")
		elif opcion == 0:
			print("Hasta luego")
			break
		else:
			print("Opción incorrecta")

except Exception as ex:
	print("Main -> {}".format(ex))