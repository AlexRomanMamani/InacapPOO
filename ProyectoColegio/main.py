from conexion.conexion import Conexion
from comandos.comandos import Comandos
import comandos.funciones as f
import hashlib
import getpass

try:
    cnx = Conexion()
    DML = Comandos(cnx.getConexion())
    login_exitoso = False #Flag

    while True:
        print(f.creaMenuLogin())
        opcion = f.n_P(2)
        if opcion == 1:
            while True: 
                nick_usuario = input("\nUsuario: ")
                pass_usuario = getpass.getpass("Contraseña: ")
                hash_pass_usuario = hashlib.md5(pass_usuario.encode("utf-8")).hexdigest()
                usuario= DML.selectUsuario(nick_usuario)
                if usuario:
                    pass_bd = usuario[0][4]
                    hash_pass_bd = hashlib.md5(pass_bd.encode()).hexdigest()

                    if hash_pass_usuario == hash_pass_bd:
                        print("Inicio de sesión exitoso")
                        print("Bienvenido {}".format(usuario[0][1]))
                        login_exitoso = True
                        codigo_acceso = usuario[0][6]
                        codigo_usuario_login = usuario[0][0]
                    else:
                        print("Contraseña incorrecta")
                        continue
                else:
                    print("Usuario no encontrado")
                    continue
                # Acceso Administrador
                if codigo_acceso == 1:
                    while True:
                        print(f.creaMenuAdministrador())
                        opcion = f.n_P(5)
                        if opcion == 1:
                            while True:
                                print(f.creaMenuMantenedorUsuarios())
                                opcion = f.n_P(5)
                                if opcion == 1:
                                    print("Crear nuevo usuario:")
                                    print("-" * 30)
                                    nombre_usuario = input("Ingrese el nombre del usuario (presione Enter para cancelar): ")
                                    if nombre_usuario == "":
                                        print("Creación de usuario cancelada.")
                                        continue
                                    apellido_usuario = input("Ingrese el apellido del usuario: ")
                                    nick_usuario = input("Ingrese el nick del usuario: ")
                                    password_usuario = getpass.getpass("Ingrese contraseña del usuario: ")
                                    hash_password_usuario = hashlib.md5(password_usuario.encode()).hexdigest()
                                    print("Ingrese el código de acceso del usuario: (1: Administrador, 2: Docente, 3: Alumno)")
                                    codigo_acceso = f.n_P(3)
                                    activo_usuario = 1
                                    DML.crearUsuario(nombre_usuario, apellido_usuario, nick_usuario, password_usuario,hash_password_usuario, codigo_acceso, activo_usuario)
                                elif opcion == 2:
                                    print("Modificar usuario:")
                                    print("-" * 30)
                                    # Mostrar usuarios
                                    if len(DML.listarUsuarios()):
                                        for usuario in DML.listarUsuarios():
                                            print("[{}]. Nombre: {}, Apellido: {}, Nick: {}, Tipo Usuario: {}".format(usuario[0], usuario[1], usuario[2], usuario[3], usuario[4]))
                                    else:
                                        print("No se encontraron registros")
                                    entrada = input("Ingrese el código del usuario a modificar (presione Enter para cancelar): ")
                                    if entrada == "":
                                        print("Modificación de usuario cancelada.")
                                        continue
                                    else:
                                        try:
                                            codigo = int(entrada)
                                            nombre_usuario = input("Ingrese el nombre del usuario: ")
                                            apellido_usuario = input("Ingrese el apellido del usuario: ")
                                            nick_usuario = input("Ingrese el nick del usuario: ")
                                            password_usuario = getpass.getpass("Ingrese contraseña del usuario: ")
                                            hash_password_usuario = hashlib.md5(password_usuario.encode()).hexdigest()
                                            DML.modificarUsuario(nombre_usuario, apellido_usuario, nick_usuario, password_usuario, hash_password_usuario, codigo)
                                        except ValueError:
                                            print("Debe ingresar un número valido.")
                                elif opcion == 3:
                                    print("Eliminar usuario:")
                                    print("-" * 30)
                                    if len(DML.listarUsuarios()):
                                        for usuario in DML.listarUsuarios():
                                            print("[{}]. Nombre: {}, Apellido: {}, Nick: {}, Tipo Usuario: {}".format(usuario[0], usuario[1], usuario[2], usuario[3], usuario[4]))
                                    else:
                                        print("No se encontraron registros")
                                    entrada = input("Ingrese el código del usuario a eliminar (presione Enter para cancelar): ")
                                    if entrada == "":
                                        print("Eliminación de usuario cancelada.")
                                        continue
                                    else:
                                        try:
                                            codigo = int(entrada)
                                            DML.eliminarUsuario(codigo)
                                        except ValueError:
                                            print("Debe ingresar un número valido.")
                                elif opcion == 4:
                                    print("Listado de todos los usuarios:")
                                    print("-" * 30)
                                    if len(DML.listarUsuarios()):
                                        for usuario in DML.listarUsuarios():
                                            print("[{}]. Nombre: {}, Apellido: {}, Nick: {}, Tipo Usuario: {}".format(usuario[0], usuario[1], usuario[2], usuario[3], usuario[4]))
                                    else:
                                        print("No se encontraron registros")
                                elif opcion == 5:
                                    break
                        elif opcion == 2:
                            while True:
                                print(f.creaMenuMantenedorAsignaturas())
                                opcion = f.n_P(12)
                                if opcion == 1:
                                    print("Crear nueva asignatura:")
                                    print("-" * 30)
                                    nombre_asignatura = input("Ingrese el nombre de la asignatura (presione Enter para cancelar): ")
                                    if nombre_asignatura == "":
                                        print("Creación de asignatura cancelada.")
                                        continue
                                    horas_asignatura = int(input("Ingrese las horas de la asignatura: "))
                                    activo_asignatura = 1
                                    DML.crearAsignatura(nombre_asignatura, horas_asignatura, activo_asignatura)
                                elif opcion == 2:
                                    print("Modificar asignatura:")
                                    print("-" * 30)
                                    # Mostrar asignaturas
                                    if len(DML.listarAsignaturas()):
                                        for asignatura in DML.listarAsignaturas():
                                            print("[{}]. Nombre: {}, Horas: {}".format(asignatura[0], asignatura[1], asignatura[2]))
                                    else:
                                        print("No se encontraron registros")
                                    entrada = input("Ingrese el código de la asignatura a modificar (presione Enter para cancelar): ")
                                    if entrada == "":
                                        print("Modificación de asignatura cancelada.")
                                        continue
                                    else:
                                        try:
                                            codigo = int(entrada)
                                            nombre_asignatura = input("Ingrese el nombre de la asignatura: ")
                                            horas_asignatura = int(input("Ingrese las horas de la asignatura: "))
                                            DML.modificarAsignatura(nombre_asignatura, horas_asignatura, codigo)
                                        except ValueError:
                                            print("Debe ingresar un número valido.")
                                elif opcion == 3:
                                    print("Eliminar asignatura:")
                                    print("-" * 30)
                                    if len(DML.listarAsignaturas()):
                                        for asignatura in DML.listarAsignaturas():
                                            print("[{}]. Nombre: {}, Horas: {}".format(asignatura[0], asignatura[1], asignatura[2]))
                                    else:
                                        print("No se encontraron registros")
                                    entrada = input("Ingrese el código de la asignatura a eliminar (presione Enter para cancelar): ")
                                    if entrada == "":
                                        print("Eliminación de asignatura cancelada.")
                                        continue
                                    else:
                                        try:
                                            codigo = int(entrada)
                                            DML.eliminarAsignatura(codigo)
                                        except ValueError:
                                            print("Debe ingresar un número valido.")
                                elif opcion == 4:
                                    print("Listado de todas las asignaturas:")
                                    print("-" * 30)
                                    if len(DML.listarAsignaturas()):
                                        for asignatura in DML.listarAsignaturas():
                                            print("[{}]. Nombre: {}, Horas: {}".format(asignatura[0], asignatura[1], asignatura[2]))
                                    else:
                                        print("No se encontraron registros")
                                elif opcion == 5:
                                    print("Agregar docente a asignatura:")
                                    print("-" * 30)
                                    # Mostrar docentes
                                    if len(DML.listarDocentes()):
                                        print("Docentes:")
                                        for docente in DML.listarDocentes():
                                            print("[{}]. Nombre: {} {}".format(docente[0], docente[1], docente[2]))
                                    else:
                                        print("No se encontraron registros")
                                    entrada = input("Ingrese el código del docente (presione Enter para cancelar): ")
                                    if entrada == "":
                                        print("Agregar docente a asignatura cancelado.")
                                        continue
                                    else:
                                        try:
                                            codigo_usuario = int(entrada)
                                            # Mostrar asignaturas
                                            if len(DML.listarAsignaturas()):
                                                print("Asignaturas:")
                                                for asignatura in DML.listarAsignaturas():
                                                    print("[{}]. Nombre: {}, Horas: {}".format(asignatura[0], asignatura[1], asignatura[2]))
                                            else:
                                                print("No se encontraron registros")
                                            codigo_asignatura = int(input("Ingrese el código de la asignatura: "))
                                            if DML.verificarDocente(codigo_usuario) and DML.verificarAsignatura(codigo_asignatura):
                                                DML.crearDocenteAsignatura(codigo_usuario, codigo_asignatura)
                                        except ValueError:
                                            print("Debe ingresar un número valido.")
                                elif opcion == 6:
                                    print("Modificar docente de una asignatura:")
                                    print("-" * 30)
                                    # Mostrar asignaturas con docentes
                                    if DML.listarAsignaturasConDocentes():
                                        print("Asignaturas:")
                                        for asignatura in DML.listarAsignaturasConDocentes():
                                            print("[{}]. Asignatura: {}".format(asignatura[0], asignatura[1]))
                                            if len(DML.listarDocentesDeUnaAsignatura(asignatura[0])):
                                                print("\tDocentes:")
                                                for docente in DML.listarDocentesDeUnaAsignatura(asignatura[0]):
                                                    print("\t\t○ {} {}".format(docente[1], docente[2]))
                                            else:
                                                print("\t\tNo hay docentes en esta asignatura")
                                    else:
                                        print("No se encontraron registros")
                                    entrada = input("Ingrese el código de la asignatura a modificar (presione Enter para cancelar): ")
                                    if entrada == "":
                                        print("Modificación de docente de asignatura cancelada.")
                                        continue
                                    else:
                                        try:
                                            codigo_asignatura = int(entrada)
                                            # Mostrar docentes
                                            if len(DML.listarDocentes()):
                                                print("Docentes:")
                                                for docente in DML.listarDocentes():
                                                    print("[{}]. Nombre: {} {}".format(docente[0], docente[1], docente[2]))
                                            else:
                                                print("No se encontraron registros")
                                            codigo_usuario = int(input("Ingrese el código del docente: "))
                                            if DML.verificarDocente(codigo_usuario) and DML.verificarAsignatura(codigo_asignatura):
                                                DML.modificarDocenteDeAsignatura(codigo_usuario, codigo_asignatura)
                                        except ValueError:
                                            print("Debe ingresar un número valido.")
                                elif opcion == 7:
                                    print("Eliminar docente de una asignatura:")
                                    print("-" * 30)
                                    # Mostrar asignaturas con docentes
                                    if DML.listarAsignaturasConDocentes():
                                        print("Asignaturas:")
                                        for asignatura in DML.listarAsignaturasConDocentes():
                                            print("[{}]. Asignatura: {} -> Docente: {} {}".format(asignatura[0], asignatura[1], asignatura[2], asignatura[3]))
                                    else:
                                        print("No se encontraron registros")
                                    entrada = input("Ingrese el código de la asignatura a consultar (presione Enter para cancelar): ")
                                    if entrada == "":
                                        print("Eliminación de docente de asignatura cancelada.")
                                        continue
                                    else:
                                        try:
                                            codigo_asignatura = int(entrada)
                                            # Mostrar docentes de una asignatura
                                            if len(DML.listarDocentesDeUnaAsignatura(codigo_asignatura)):
                                                print("Docentes de la Asignatura:")
                                                for docente in DML.listarDocentesDeUnaAsignatura(codigo_asignatura):
                                                    print("[{}]. Nombre: {} {}".format(docente[0], docente[1], docente[2]))
                                            else:
                                                print("No se encontraron registros")
                                            codigo_usuario = int(input("Ingrese el código del docente que desea eliminar: "))
                                            if DML.verificarDocente(codigo_usuario) and DML.verificarAsignatura(codigo_asignatura):
                                                DML.eliminarDocenteAsignatura(codigo_usuario, codigo_asignatura)
                                        except ValueError:
                                            print("Debe ingresar un número valido.")
                                elif opcion == 8:
                                    print("Listar asignaturas con sus respectivos docentes y alumnos:")
                                    print("-" * 30)
                                    # Mostrar asignaturas
                                    if len(DML.listarAsignaturas()):
                                        for asignatura in DML.listarAsignaturas():
                                            print("Asignatura: {} [cod. {}]".format(asignatura[1], asignatura[0]))
                                            if len(DML.listarDocentesDeUnaAsignatura(asignatura[0])):
                                                print("\tDocentes:")
                                                for docente in DML.listarDocentesDeUnaAsignatura(asignatura[0]):
                                                    print("\t\t○ {} {}".format(docente[1], docente[2]))
                                                    if len(DML.listarAlumnosDeUnaAsignatura(asignatura[0])):
                                                        print("\tAlumnos:")
                                                        for alumno in DML.listarAlumnosDeUnaAsignatura(asignatura[0]):
                                                            print("\t\t○ {} {}".format(alumno[1], alumno[2]))
                                                    else:
                                                        print("\t\tNo hay alumnos en esta asignatura")
                                            else:
                                                print("\t\tNo hay docentes en esta asignatura")
                                    else:
                                        print("No se encontraron registros")
                                elif opcion == 9:
                                    print("Agregar alumno a asignatura:")
                                    print("-" * 30)
                                    if len(DML.listarAlumnos()):
                                        print("Alumnos:")
                                        for alumno in DML.listarAlumnos():
                                            print("[{}]. Nombre: {} {}".format(alumno[0], alumno[1], alumno[2]))
                                    else:
                                        print("No se encontraron registros")
                                    entrada = input("Ingrese el código del alumno (presione Enter para cancelar): ")
                                    if entrada == "":
                                        print("Agregar alumno a asignatura cancelado.")
                                        continue
                                    else:
                                        try:
                                            codigo_usuario = int(entrada)
                                            # Mostrar asignaturas
                                            if len(DML.listarAsignaturas()):
                                                print("Asignaturas:")
                                                for asignatura in DML.listarAsignaturas():
                                                    print("[{}]. Nombre: {}, Horas: {}".format(asignatura[0], asignatura[1], asignatura[2]))
                                            else:
                                                print("No se encontraron registros")
                                            codigo_asignatura = int(input("Ingrese el código de la asignatura: "))
                                            if DML.verificarAlumno(codigo_usuario) and DML.verificarAsignatura(codigo_asignatura):
                                                DML.crearAlumnoAsignatura(codigo_usuario, codigo_asignatura)
                                        except ValueError:
                                            print("Debe ingresar un número valido.")
                                elif opcion == 10:
                                    print("Modificar alumno de una asignatura:")
                                    print("-" * 30)
                                    # Mostrar asignaturas con alumnos
                                    if DML.listarAsignaturasConAlumnos():
                                        print("Asignaturas:")
                                        for asignatura in DML.listarAsignaturasConAlumnos():
                                            print("[{}]. Asignatura: {} -> Alumno: {} {}".format(asignatura[0], asignatura[1], asignatura[2], asignatura[3]))
                                    else:
                                        print("No se encontraron registros")
                                    entrada = input("Ingrese el código de la asignatura a modificar (presione Enter para cancelar): ")
                                    if entrada == "":
                                        print("Modificación de alumno de asignatura cancelada.")
                                        continue
                                    else:
                                        try:
                                            codigo_asignatura = int(entrada)
                                            # Mostrar alumnos
                                            if len(DML.listarAlumnos()):
                                                print("Alumnos:")
                                                for alumno in DML.listarAlumnos():
                                                    print("[{}]. Nombre: {} {}".format(alumno[0], alumno[1], alumno[2]))
                                            else:
                                                print("No se encontraron registros")
                                            codigo_usuario = int(input("Ingrese el código del alumno: "))
                                            if DML.verificarAlumno(codigo_usuario) and DML.verificarAsignatura(codigo_asignatura):
                                                DML.modificarAlumnoDeAsignatura(codigo_usuario, codigo_asignatura)
                                        except ValueError:
                                            print("Debe ingresar un número valido.")
                                elif opcion == 11:
                                    print("Eliminar alumno de una asignatura:")
                                    print("-" * 30)
                                    # Mostrar asignaturas con alumnos
                                    if DML.listarAsignaturasConAlumnos():
                                        print("Asignaturas:")
                                        for asignatura in DML.listarAsignaturasConAlumnos():
                                            print("[{}]. Asignatura: {} -> Alumno: {} {}".format(asignatura[0], asignatura[1], asignatura[2], asignatura[3]))
                                    else:
                                        print("No se encontraron registros")
                                    entrada = input("Ingrese el código de la asignatura a consultar (presione Enter para cancelar): ")
                                    if entrada == "":
                                        print("Eliminación de alumno de asignatura cancelada.")
                                        continue
                                    else:
                                        try:
                                            codigo_asignatura = int(entrada)
                                            # Mostrar alumnos de una asignatura
                                            if len(DML.listarAlumnosDeUnaAsignatura(codigo_asignatura)):
                                                print("Alumnos de la Asignatura:")
                                                for alumno in DML.listarAlumnosDeUnaAsignatura(codigo_asignatura):
                                                    print("[{}]. Nombre: {} {}".format(alumno[0], alumno[1], alumno[2]))
                                            else:
                                                print("No se encontraron registros")
                                            codigo_usuario = int(input("Ingrese el código del alumno que desea eliminar: "))
                                            if DML.verificarAlumno(codigo_usuario) and DML.verificarAsignatura(codigo_asignatura):
                                                DML.eliminarAlumnoAsignatura(codigo_usuario, codigo_asignatura)
                                        except ValueError:
                                            print("Debe ingresar un número valido.")
                                elif opcion == 12:
                                    break
                        elif opcion == 3:
                            while True:
                                print(f.creaMenuNotas())
                                opcion = f.n_P(4)
                                if opcion == 1:
                                    print("Ingresar notas:")
                                    print("-" * 30)
                                    # Mostrar asignaturas
                                    if len(DML.listarAsignaturas()):
                                        print("Asignaturas:")
                                        for asignatura in DML.listarAsignaturas():
                                            print("[{}]. Nombre: {}".format(asignatura[0], asignatura[1]))
                                            # Contar alumnos de una asignatura
                                            if len(DML.listarAlumnosDeUnaAsignatura(asignatura[0])):
                                                print("\tAlumnos: {}".format(len(DML.listarAlumnosDeUnaAsignatura(asignatura[0]))))
                                            else:
                                                print("\tAsignatura sin alumnos")
                                    else:
                                        print("No se encontraron registros")
                                    entrada = input("Ingrese el código de la asignatura (presione Enter para cancelar): ")
                                    if entrada == "":
                                        print("Ingreso de nota cancelado.")
                                        continue
                                    else:
                                        try:
                                            codigo_asignatura = int(entrada)
                                            # Mostrar alumnos de una asignatura
                                            if len(DML.listarAlumnosDeUnaAsignatura(codigo_asignatura)):
                                                print("Alumnos de la Asignatura:")
                                                for alumno in DML.listarAlumnosDeUnaAsignatura(codigo_asignatura):
                                                    print("[{}]. Nombre: {} {}".format(alumno[0], alumno[1], alumno[2]))
                                                codigo_usuario = int(input("Ingrese el código del alumno: "))
                                                if DML.verificarAlumno(codigo_usuario) and DML.verificarAsignatura(codigo_asignatura):
                                                    nota1 = float(input("Ingrese la nota 1 del alumno: "))
                                                    nota2 = float(input("Ingrese la nota 2 del alumno: "))
                                                    nota3 = float(input("Ingrese la nota 3 del alumno: "))
                                                    DML.crearNota(nota1, nota2, nota3, codigo_usuario, codigo_asignatura)
                                            else:
                                                print("No se encontraron registros")
                                        except ValueError:
                                            print("Debe ingresar un número valido.")
                                elif opcion == 2:
                                    print("Modificar notas:")
                                    print("-" * 30)
                                    # Mostrar asignaturas
                                    if len(DML.listarAsignaturas()):
                                        print("Asignaturas:")
                                        for asignatura in DML.listarAsignaturas():
                                            print("[{}]. Nombre: {}".format(asignatura[0], asignatura[1]))
                                            # Contar alumnos de una asignatura
                                            if len(DML.listarAlumnosDeUnaAsignatura(asignatura[0])):
                                                print("\tAlumnos: {}".format(len(DML.listarAlumnosDeUnaAsignatura(asignatura[0]))))
                                            else:
                                                print("\tAsignatura sin alumnos")
                                        entrada = input("Ingrese el código de la asignatura (presione Enter para cancelar): ")
                                        if entrada == "":
                                            print("Modificación de nota cancelada.")
                                            continue
                                        else:
                                            try:
                                                codigo_asignatura = int(entrada)
                                                # Mostrar alumnos de una asignatura
                                                if len(DML.listarAlumnosDeUnaAsignatura(codigo_asignatura)):
                                                    print("Alumnos de la Asignatura:")
                                                    for alumno in DML.listarAlumnosDeUnaAsignatura(codigo_asignatura):
                                                        print("[{}]. Nombre: {} {}".format(alumno[0], alumno[1], alumno[2]))
                                                        notas = DML.listarNotasAlumnoAsignatura(alumno[0],codigo_asignatura)
                                                        if notas:
                                                            print("Notas:")
                                                            for nota in notas:
                                                                print("\tNota 1: {}, Nota 2: {}, Nota 3: {}".format(nota[0], nota[1], nota[2]))
                                                    codigo_usuario = int(input("Ingrese el código del alumno: "))
                                                    if DML.verificarAlumno(codigo_usuario) and DML.verificarAsignatura(codigo_asignatura):
                                                        nota1 = float(input("Ingrese la nota 1 del alumno: "))
                                                        nota2 = float(input("Ingrese la nota 2 del alumno: "))
                                                        nota3 = float(input("Ingrese la nota 3 del alumno: "))
                                                        DML.crearNota(nota1, nota2, nota3, codigo_usuario, codigo_asignatura)
                                                else:
                                                    print("No se encontraron registros")
                                            except ValueError:
                                                print("Debe ingresar un número valido.")
                                    else:
                                        print("No se encontraron registros")
                                elif opcion == 3:
                                    print("Eliminar notas:")
                                    print("-" * 30)
                                    # Mostrar asignaturas
                                    if len(DML.listarAsignaturas()):
                                        print("Asignaturas:")
                                        for asignatura in DML.listarAsignaturas():
                                            print("[{}]. Nombre: {}".format(asignatura[0], asignatura[1]))
                                            # Contar alumnos de una asignatura
                                            if len(DML.listarAlumnosDeUnaAsignatura(asignatura[0])):
                                                print("\tAlumnos: {}".format(len(DML.listarAlumnosDeUnaAsignatura(asignatura[0]))))
                                            else:
                                                print("\tAsignatura sin alumnos")
                                        entrada = input("Ingrese el código de la asignatura (presione Enter para cancelar): ")
                                        if entrada == "":
                                            print("Eliminación de nota cancelada.")
                                            continue
                                        else:
                                            try:
                                                codigo_asignatura = int(entrada)
                                                # Mostrar alumnos de una asignatura
                                                if len(DML.listarAlumnosDeUnaAsignatura(codigo_asignatura)):
                                                    print("Alumnos de la Asignatura:")
                                                    for alumno in DML.listarAlumnosDeUnaAsignatura(codigo_asignatura):
                                                        print("[{}]. Nombre: {} {}".format(alumno[0], alumno[1], alumno[2]))
                                                        notas = DML.listarNotasAlumnoAsignatura(alumno[0],codigo_asignatura)
                                                        if notas:
                                                            print("Notas:")
                                                            for nota in notas:
                                                                print("\tNota 1: {}, Nota 2: {}, Nota 3: {}".format(nota[0], nota[1], nota[2]))
                                                    codigo_usuario = int(input("Ingrese el código del alumno: "))
                                                    if DML.verificarAlumno(codigo_usuario) and DML.verificarAsignatura(codigo_asignatura):
                                                        DML.eliminarNotasAlumnoAsignatura(codigo_usuario, codigo_asignatura)
                                                else:
                                                    print("No se encontraron registros")
                                            except ValueError:
                                                print("Debe ingresar un número valido.")
                                    else:
                                        print("No se encontraron registros")
                                elif opcion == 4:
                                    break
                        elif opcion == 4:
                            print(f.creaMenuAsistencia())
                            opcion = f.n_P(4)
                            if opcion == 1:
                                print("Ingresar asistencia:")
                                print("-" * 30)
                                # Mostrar asignaturas
                                if len(DML.listarAsignaturas()):
                                    print("Asignaturas:")
                                    for asignatura in DML.listarAsignaturas():
                                        print("[{}]. Nombre: {}".format(asignatura[0], asignatura[1]))
                                        # Contar alumnos de una asignatura
                                        if len(DML.listarAlumnosDeUnaAsignatura(asignatura[0])):
                                            print("\tAlumnos: {}".format(len(DML.listarAlumnosDeUnaAsignatura(asignatura[0]))))
                                        else:
                                            print("\tAsignatura sin alumnos")
                                    entrada = input("Ingrese el código de la asignatura (presione Enter para cancelar): ")
                                    if entrada == "":
                                        print("Ingreso de asistencia cancelado.")
                                        continue
                                    else:
                                        try:
                                            codigo_asignatura = int(entrada)
                                            # Mostrar alumnos de una asignatura
                                            if len(DML.listarAlumnosDeUnaAsignatura(codigo_asignatura)):
                                                print("Alumnos de la Asignatura:")
                                                for alumno in DML.listarAlumnosDeUnaAsignatura(codigo_asignatura):
                                                    print("[{}]. Nombre: {} {}".format(alumno[0], alumno[1], alumno[2]))
                                                codigo_usuario = int(input("Ingrese el código del alumno: "))
                                                asistencia = int(input("Ingrese la asistencia del alumno: "))
                                                if DML.verificarAlumno(codigo_usuario) and DML.verificarAsignatura(codigo_asignatura):
                                                    DML.crearAsistencia(asistencia, codigo_usuario, codigo_asignatura)
                                                else:
                                                    print("Usuario o asignatura incorrectos")
                                            else:
                                                print("No se encontraron registros")
                                        except ValueError:
                                            print("Debe ingresar un número valido.")
                                else:
                                    print("No se encontraron registros")
                            elif opcion == 2:
                                print("Modificar asistencia:")
                                print("-" * 30)
                                # Mostrar asignaturas
                                if len(DML.listarAsignaturas()):
                                    print("Asignaturas:")
                                    for asignatura in DML.listarAsignaturas():
                                        print("[{}]. Nombre: {}".format(asignatura[0], asignatura[1]))
                                        # Contar alumnos de una asignatura
                                        if len(DML.listarAlumnosDeUnaAsignatura(asignatura[0])):
                                            print("\tAlumnos: {}".format(len(DML.listarAlumnosDeUnaAsignatura(asignatura[0]))))
                                        else:
                                            print("\tAsignatura sin alumnos")
                                    entrada = input("Ingrese el código de la asignatura (presione Enter para cancelar): ")
                                    if entrada == "":
                                        print("Modificación de asistencia cancelada.")
                                        continue
                                    else:
                                        try:
                                            codigo_asignatura = int(entrada)
                                            # Mostrar alumnos de una asignatura
                                            if len(DML.listarAlumnosDeUnaAsignatura(codigo_asignatura)):
                                                print("Alumnos de la Asignatura:")
                                                for alumno in DML.listarAlumnosDeUnaAsignatura(codigo_asignatura):
                                                    print("[{}]. Nombre: {} {}".format(alumno[0], alumno[1], alumno[2]))
                                                    asistencia = DML.listarAsistenciaAlumnoAsignatura(alumno[0],codigo_asignatura)
                                                    print("\tAsistencia: {}".format(asistencia[0]))
                                                codigo_usuario = int(input("Ingrese el código del alumno: "))
                                                asistencia = int(input("Ingrese la asistencia del alumno: "))
                                                if DML.verificarAlumno(codigo_usuario) and DML.verificarAsignatura(codigo_asignatura):
                                                    DML.crearAsistencia(asistencia, codigo_usuario, codigo_asignatura)
                                                else:
                                                    print("Usuario o asignatura incorrectos")
                                            else:
                                                print("No se encontraron registros")
                                        except ValueError:
                                            print("Debe ingresar un número valido.")
                                else:
                                    print("No se encontraron registros")
                            elif opcion == 3:
                                print("Eliminar asistencia:")
                                print("-" * 30)
                                # Mostrar asignaturas
                                if len(DML.listarAsignaturas()):
                                    print("Asignaturas:")
                                    for asignatura in DML.listarAsignaturas():
                                        print("[{}]. Nombre: {}".format(asignatura[0], asignatura[1]))
                                        # Contar alumnos de una asignatura
                                        if len(DML.listarAlumnosDeUnaAsignatura(asignatura[0])):
                                            print("\tAlumnos: {}".format(len(DML.listarAlumnosDeUnaAsignatura(asignatura[0]))))
                                        else:
                                            print("\tAsignatura sin alumnos")
                                    entrada = input("Ingrese el código de la asignatura (presione Enter para cancelar): ")
                                    if entrada == "":
                                        print("Eliminación de asistencia cancelada.")
                                        continue
                                    else:
                                        try:
                                            codigo_asignatura = int(entrada)
                                            # Mostrar alumnos de una asignatura
                                            if len(DML.listarAlumnosDeUnaAsignatura(codigo_asignatura)):
                                                print("Alumnos de la Asignatura:")
                                                for alumno in DML.listarAlumnosDeUnaAsignatura(codigo_asignatura):
                                                    print("[{}]. Nombre: {} {}".format(alumno[0], alumno[1], alumno[2]))
                                                    asistencia = DML.listarAsistenciaAlumnoAsignatura(alumno[0],codigo_asignatura)
                                                    print("\tAsistencia: {}".format(asistencia[0]))
                                                codigo_usuario = int(input("Ingrese el código del alumno: "))
                                                if DML.verificarAlumno(codigo_usuario) and DML.verificarAsignatura(codigo_asignatura):
                                                    DML.eliminarAsistenciaAlumnoAsignatura(codigo_usuario, codigo_asignatura)
                                            else:
                                                print("No se encontraron registros")
                                        except ValueError:
                                            print("Debe ingresar un número valido.")
                                else:
                                    print("No se encontraron registros")
                            elif opcion == 4:
                                break
                        elif opcion == 5:
                            break
                # Acceso Docente
                elif codigo_acceso == 2:
                    while True:
                        print(f.creaMenuDocente())
                        opcion = f.n_P(4)
                        if opcion == 1:
                            while True:
                                print(f.creaMenuNotas())
                                opcion = f.n_P(4)
                                if opcion == 1:
                                    print("Ingresar notas:")
                                    print("-" * 30)
                                    # Mostrar asignaturas
                                    if len(DML.listarAsignaturasACargo(codigo_usuario_login)):
                                        print("Asignaturas:")
                                        for asignatura in DML.listarAsignaturasACargo(codigo_usuario_login):
                                            print("[{}]. Nombre: {}".format(asignatura[0], asignatura[1]))
                                            # Contar alumnos de una asignatura
                                            if len(DML.listarAlumnosDeUnaAsignatura(asignatura[0])):
                                                print("\tAlumnos: {}".format(len(DML.listarAlumnosDeUnaAsignatura(asignatura[0]))))
                                            else:
                                                print("\tAsignatura sin alumnos")
                                    else:
                                        print("No se encontraron registros")
                                    entrada = input("Ingrese el código de la asignatura (presione Enter para cancelar): ")
                                    if entrada == "":
                                        print("Ingreso de nota cancelado.")
                                        continue
                                    else:
                                        try:
                                            codigo_asignatura = int(entrada)
                                            # Mostrar alumnos de una asignatura
                                            if len(DML.listarAlumnosDeUnaAsignatura(codigo_asignatura)):
                                                print("Alumnos de la Asignatura:")
                                                for alumno in DML.listarAlumnosDeUnaAsignatura(codigo_asignatura):
                                                    print("[{}]. Nombre: {} {}".format(alumno[0], alumno[1], alumno[2]))
                                                codigo_usuario = int(input("Ingrese el código del alumno: "))
                                                if DML.verificarAlumno(codigo_usuario) and DML.verificarAsignatura(codigo_asignatura):
                                                    nota1 = float(input("Ingrese la nota 1 del alumno: "))
                                                    nota2 = float(input("Ingrese la nota 2 del alumno: "))
                                                    nota3 = float(input("Ingrese la nota 3 del alumno: "))
                                                    DML.crearNota(nota1, nota2, nota3, codigo_usuario, codigo_asignatura)
                                                else:
                                                    print("Usuario o asignatura incorrectos")
                                            else:
                                                print("No se encontraron registros")
                                        except ValueError:
                                            print("Debe ingresar un número valido.")
                                elif opcion == 2:
                                    print("Modificar notas:")
                                    print("-" * 30)
                                    # Mostrar asignaturas
                                    if len(DML.listarAsignaturasACargo(codigo_usuario_login)):
                                        print("Asignaturas:")
                                        for asignatura in DML.listarAsignaturasACargo(codigo_usuario_login):
                                            print("[{}]. Nombre: {}".format(asignatura[0], asignatura[1]))
                                            # Contar alumnos de una asignatura
                                            if len(DML.listarAlumnosDeUnaAsignatura(asignatura[0])):
                                                print("\tAlumnos: {}".format(len(DML.listarAlumnosDeUnaAsignatura(asignatura[0]))))
                                            else:
                                                print("\tAsignatura sin alumnos")
                                        entrada = input("Ingrese el código de la asignatura (presione Enter para cancelar): ")
                                        if entrada == "":
                                            print("Modificación de nota cancelada.")
                                            continue
                                        else:
                                            try:
                                                codigo_asignatura = int(entrada)
                                                # Mostrar alumnos de una asignatura
                                                if len(DML.listarAlumnosDeUnaAsignatura(codigo_asignatura)):
                                                    print("Alumnos de la Asignatura:")
                                                    for alumno in DML.listarAlumnosDeUnaAsignatura(codigo_asignatura):
                                                        print("[{}]. Nombre: {} {}".format(alumno[0], alumno[1], alumno[2]))
                                                        notas = DML.listarNotasAlumnoAsignatura(alumno[0],codigo_asignatura)
                                                        if notas:
                                                            print("Notas:")
                                                            for nota in notas:
                                                                print("\tNota 1: {}, Nota 2: {}, Nota 3: {}".format(nota[0], nota[1], nota[2]))
                                                    codigo_usuario = int(input("Ingrese el código del alumno: "))
                                                    if DML.verificarAlumno(codigo_usuario) and DML.verificarAsignatura(codigo_asignatura):
                                                        nota1 = float(input("Ingrese la nota 1 del alumno: "))
                                                        nota2 = float(input("Ingrese la nota 2 del alumno: "))
                                                        nota3 = float(input("Ingrese la nota 3 del alumno: "))
                                                        DML.crearNota(nota1, nota2, nota3, codigo_usuario, codigo_asignatura)
                                                else:
                                                    print("No se encontraron registros")
                                            except ValueError:
                                                print("Debe ingresar un número valido.")
                                    else:
                                        print("No se encontraron registros")
                                elif opcion == 3:
                                    print("Eliminar notas:")
                                    print("-" * 30)
                                    # Mostrar asignaturas
                                    if len(DML.listarAsignaturasACargo(codigo_usuario_login)):
                                        print("Asignaturas:")
                                        for asignatura in DML.listarAsignaturasACargo(codigo_usuario_login):
                                            print("[{}]. Nombre: {}".format(asignatura[0], asignatura[1]))
                                            # Contar alumnos de una asignatura
                                            if len(DML.listarAlumnosDeUnaAsignatura(asignatura[0])):
                                                print("\tAlumnos: {}".format(len(DML.listarAlumnosDeUnaAsignatura(asignatura[0]))))
                                            else:
                                                print("\tAsignatura sin alumnos")
                                        entrada = input("Ingrese el código de la asignatura (presione Enter para cancelar): ")
                                        if entrada == "":
                                            print("Eliminación de nota cancelada.")
                                            continue
                                        else:
                                            try:
                                                codigo_asignatura = int(entrada)
                                                # Mostrar alumnos de una asignatura
                                                if len(DML.listarAlumnosDeUnaAsignatura(codigo_asignatura)):
                                                    print("Alumnos de la Asignatura:")
                                                    for alumno in DML.listarAlumnosDeUnaAsignatura(codigo_asignatura):
                                                        print("[{}]. Nombre: {} {}".format(alumno[0], alumno[1], alumno[2]))
                                                        notas = DML.listarNotasAlumnoAsignatura(alumno[0],codigo_asignatura)
                                                        if notas:
                                                            print("Notas:")
                                                            for nota in notas:
                                                                print("\tNota 1: {}, Nota 2: {}, Nota 3: {}".format(nota[0], nota[1], nota[2]))
                                                    codigo_usuario = int(input("Ingrese el código del alumno: "))
                                                    if DML.verificarAlumno(codigo_usuario) and DML.verificarAsignatura(codigo_asignatura):
                                                        DML.eliminarNotasAlumnoAsignatura(codigo_usuario, codigo_asignatura)
                                                else:
                                                    print("No se encontraron registros")
                                            except ValueError:
                                                print("Debe ingresar un número valido.")
                                    else:
                                        print("No se encontraron registros")
                                elif opcion == 4:
                                    break
                        elif opcion == 2:
                            print(f.creaMenuAsistencia())
                            opcion = f.n_P(4)
                            if opcion == 1:
                                print("Ingresar asistencia:")
                                print("-" * 30)
                                # Mostrar asignaturas
                                if len(DML.listarAsignaturasACargo(codigo_usuario_login)):
                                    print("Asignaturas:")
                                    for asignatura in DML.listarAsignaturasACargo(codigo_usuario_login):
                                        print("[{}]. Nombre: {}".format(asignatura[0], asignatura[1]))
                                        # Contar alumnos de una asignatura
                                        if len(DML.listarAlumnosDeUnaAsignatura(asignatura[0])):
                                            print("\tAlumnos: {}".format(len(DML.listarAlumnosDeUnaAsignatura(asignatura[0]))))
                                        else:
                                            print("\tAsignatura sin alumnos")
                                    entrada = input("Ingrese el código de la asignatura (presione Enter para cancelar): ")
                                    if entrada == "":
                                        print("Ingreso de asistencia cancelado.")
                                        continue
                                    else:
                                        try:
                                            codigo_asignatura = int(entrada)
                                            # Mostrar alumnos de una asignatura
                                            if len(DML.listarAlumnosDeUnaAsignatura(codigo_asignatura)):
                                                print("Alumnos de la Asignatura:")
                                                for alumno in DML.listarAlumnosDeUnaAsignatura(codigo_asignatura):
                                                    print("[{}]. Nombre: {} {}".format(alumno[0], alumno[1], alumno[2]))
                                                codigo_usuario = int(input("Ingrese el código del alumno: "))
                                                asistencia = int(input("Ingrese la asistencia del alumno: "))
                                                if DML.verificarAlumno(codigo_usuario) and DML.verificarAsignatura(codigo_asignatura):
                                                    DML.crearAsistencia(asistencia, codigo_usuario, codigo_asignatura)
                                                else:
                                                    print("Usuario o asignatura incorrectos")
                                            else:
                                                print("No se encontraron registros")
                                        except ValueError:
                                            print("Debe ingresar un número valido.")
                                else:
                                    print("No se encontraron registros")
                            elif opcion == 2:
                                print("Modificar asistencia:")
                                print("-" * 30)
                                # Mostrar asignaturas
                                if len(DML.listarAsignaturasACargo(codigo_usuario_login)):
                                    print("Asignaturas:")
                                    for asignatura in DML.listarAsignaturasACargo(codigo_usuario_login):
                                        print("[{}]. Nombre: {}".format(asignatura[0], asignatura[1]))
                                        # Contar alumnos de una asignatura
                                        if len(DML.listarAlumnosDeUnaAsignatura(asignatura[0])):
                                            print("\tAlumnos: {}".format(len(DML.listarAlumnosDeUnaAsignatura(asignatura[0]))))
                                        else:
                                            print("\tAsignatura sin alumnos")
                                    entrada = input("Ingrese el código de la asignatura (presione Enter para cancelar): ")
                                    if entrada == "":
                                        print("Modificación de asistencia cancelada.")
                                        continue
                                    else:
                                        try:
                                            codigo_asignatura = int(entrada)
                                            # Mostrar alumnos de una asignatura
                                            if len(DML.listarAlumnosDeUnaAsignatura(codigo_asignatura)):
                                                print("Alumnos de la Asignatura:")
                                                for alumno in DML.listarAlumnosDeUnaAsignatura(codigo_asignatura):
                                                    print("[{}]. Nombre: {} {}".format(alumno[0], alumno[1], alumno[2]))
                                                    asistencia = DML.listarAsistenciaAlumnoAsignatura(alumno[0],codigo_asignatura)
                                                    print("\tAsistencia: {}".format(asistencia[0]))
                                                codigo_usuario = int(input("Ingrese el código del alumno: "))
                                                asistencia = int(input("Ingrese la asistencia del alumno: "))
                                                if DML.verificarAlumno(codigo_usuario) and DML.verificarAsignatura(codigo_asignatura):
                                                    DML.crearAsistencia(asistencia, codigo_usuario, codigo_asignatura)
                                                else:
                                                    print("Usuario o asignatura incorrectos")
                                            else:
                                                print("No se encontraron registros")
                                        except ValueError:
                                            print("Debe ingresar un número valido.")
                                else:
                                    print("No se encontraron registros")
                            elif opcion == 3:
                                print("Eliminar asistencia:")
                                print("-" * 30)
                                # Mostrar asignaturas
                                if len(DML.listarAsignaturasACargo(codigo_usuario_login)):
                                    print("Asignaturas:")
                                    for asignatura in DML.listarAsignaturasACargo(codigo_usuario_login):
                                        print("[{}]. Nombre: {}".format(asignatura[0], asignatura[1]))
                                        # Contar alumnos de una asignatura
                                        if len(DML.listarAlumnosDeUnaAsignatura(asignatura[0])):
                                            print("\tAlumnos: {}".format(len(DML.listarAlumnosDeUnaAsignatura(asignatura[0]))))
                                        else:
                                            print("\tAsignatura sin alumnos")
                                    entrada = input("Ingrese el código de la asignatura (presione Enter para cancelar): ")
                                    if entrada == "":
                                        print("Eliminación de asistencia cancelada.")
                                        continue
                                    else:
                                        try:
                                            codigo_asignatura = int(entrada)
                                            # Mostrar alumnos de una asignatura
                                            if len(DML.listarAlumnosDeUnaAsignatura(codigo_asignatura)):
                                                print("Alumnos de la Asignatura:")
                                                for alumno in DML.listarAlumnosDeUnaAsignatura(codigo_asignatura):
                                                    print("[{}]. Nombre: {} {}".format(alumno[0], alumno[1], alumno[2]))
                                                    asistencia = DML.listarAsistenciaAlumnoAsignatura(alumno[0],codigo_asignatura)
                                                    print("\tAsistencia: {}".format(asistencia[0]))
                                                codigo_usuario = int(input("Ingrese el código del alumno: "))
                                                if DML.verificarAlumno(codigo_usuario) and DML.verificarAsignatura(codigo_asignatura):
                                                    DML.eliminarAsistenciaAlumnoAsignatura(codigo_usuario, codigo_asignatura)
                                            else:
                                                print("No se encontraron registros")
                                        except ValueError:
                                            print("Debe ingresar un número valido.")
                                else:
                                    print("No se encontraron registros")
                            elif opcion == 4:
                                break
                        elif opcion == 3:
                            print("Listar Asignaturas y Alumnos:")
                            print("-" * 30)
                            # Mostrar asignaturas
                            if len(DML.listarAsignaturasACargo(codigo_usuario_login)):
                                for asignatura in DML.listarAsignaturasACargo(codigo_usuario_login):
                                    print("Asignatura: {} [cod. {}]".format(asignatura[1], asignatura[0]))
                                    if len(DML.listarAlumnosDeUnaAsignatura(asignatura[0])):
                                        print("\tAlumnos:")
                                        for alumno in DML.listarAlumnosDeUnaAsignatura(asignatura[0]):
                                            print("\t○ {} {}".format(alumno[1], alumno[2]))
                                    else:
                                        print("\tNo hay alumnos en esta asignatura")
                        elif opcion == 4:
                            break
                # Acceso Alumno
                elif codigo_acceso == 3:
                    while True:
                        print(f.creaMenuAlumno())
                        opcion = f.n_P(2)
                        if opcion == 1:
                            print("Listar Asignaturas, Notas y Asistencia:")
                            print("-"*30)
                            # Mostrar asignaturas
                            if len(DML.listarAsignaturasDeAlumno(codigo_usuario_login)):
                                for asignatura in DML.listarAsignaturasDeAlumno(codigo_usuario_login):
                                    print("Asignatura: {} [cod. {}]".format(asignatura[1], asignatura[0]))
                                    if len(DML.listarNotasAlumnoAsignatura(codigo_usuario_login, asignatura[0])):
                                        for nota in DML.listarNotasAlumnoAsignatura(codigo_usuario_login, asignatura[0]):
                                            print("\t○ Nota 1: {}, Nota 2: {}, Nota 3: {}".format(nota[0], nota[1], nota[2]))
                                    else:
                                        print("\tNo hay notas en esta asignatura")
                                    if len(DML.listarAsistenciaAlumnoAsignatura(codigo_usuario_login, asignatura[0])):
                                        print("\t○ Asistencia: {}".format(DML.listarAsistenciaAlumnoAsignatura(codigo_usuario_login, asignatura[0])[0]))
                                    else:
                                        print("\tNo hay asistencia en esta asignatura")
                            else:
                                print("No se encontraron registros")
                        elif opcion == 2:
                            break
                if login_exitoso:
                    break
        elif opcion == 2:
            print("Saliendo...")
            break
except Exception as ex:
    print("Main -> {}".format(ex)) 