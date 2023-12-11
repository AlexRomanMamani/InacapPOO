import time
def creaMenuAlumno():
    '''Crea el menu del alumno''' 
    return """\n----\033[1m\033[42m\033[37m M E N U  A L U M N O \033[0m\033[0m\033[0m----\n
    1 ---- Listar Asignaturas (Notas y Asistencia)
    2 ---- Cerrar sesión\n"""
def creaMenuDocente():
    '''Crea el menu del docente''' 
    return """\n----\033[1m\033[42m\033[37m M E N U  D O C E N T E \033[0m\033[0m\033[0m----\n
    1 ---- Mantenedor de Notas
    2 ---- Mantenedor de Asistencia
    3 ---- Listar Asignaturas con Alumnos
    4 ---- Cerar sesión\n"""
def creaMenuAsistencia():
    '''Crea el menu de asistencia''' 
    return """\n----\033[1m\033[42m\033[37m M A N T E N E D O R  A S I S T E N C I A \033[0m\033[0m\033[0m----\n
    1 ---- Ingresar asistencia
    2 ---- Modificar asistencia
    3 ---- Eliminar asistencia
    4 ---- Volver\n""" 
def creaMenuNotas():
    '''Crea el menu de notas''' 
    return """\n----\033[1m\033[42m\033[37m M A N T E N E D O R  N O T A S \033[0m\033[0m\033[0m----\n
    1 ---- Ingresar notas
    2 ---- Modificar notas
    3 ---- Eliminar notas
    4 ---- Volver\n"""    
def creaMenuAdministrador():
    '''Crea el menu del administrador''' 
    return """\n----\033[1m\033[42m\033[37m M E N U  A D M I N I S T R A D O R \033[0m\033[0m\033[0m----\n
    1 ---- Mantenedor de Usuarios
    2 ---- Mantenedor de Asignaturas
    3 ---- Mantenedor de Notas
    4 ---- Mantenedor de Asistencia
    5 ---- Cerrar sesión\n"""
def creaMenuMantenedorUsuarios():
    '''Crea el menu del Mantenedor de Usuarios''' 
    return """\n----\033[1m\033[42m\033[37m M A N T E N E D O R  U S U A R I O S \033[0m\033[0m\033[0m----\n
    1 ---- Crear nuevo usuario
    2 ---- Modificar usuario
    3 ---- Eliminar usuario
    4 ---- Listar usuarios
    5 ---- Volver\n"""
def creaMenuMantenedorAsignaturas():
    '''Crea el menu del Mantenedor de Asignaturas''' 
    return """\n----\033[1m\033[42m\033[37m M A N T E N E D O R  A S I G N A T U R A S \033[0m\033[0m\033[0m----\n
    1 ---- Crear nueva asignatura      5 ---- Agregar docente a asignatura                  9  ---- Agregar alumno a asignatura
    2 ---- Modificar asignatura        6 ---- Modificar docente de asignatura               10 ---- Modificar alumno de asignatura
    3 ---- Eliminar asignatura         7 ---- Eliminar docente de asignatura                11 ---- Eliminar alumno de asignatura
    4 ---- Listar asignaturas          8 ---- Listar Asignaturas con Docentes y Alumnos     12 ---- Volver\n"""
def creaMenuLogin():
    '''Crea el menu del Login''' 
    return """\n----\033[1m\033[42m\033[37m L O G I N \033[0m\033[0m\033[0m----\n
    1 ---- Iniciar sesión
    2 ---- Salir\n"""
def n_P(max_option): # max_option = maxima opcion, Ingrese opcion
    while True:
        try:
            o = int(input(f"Ingrese opción (1-{max_option}): "))
            if o < 1 or o > max_option:
                print(f"\033[91m\033[107m>>>\033[0m Error, solo se permite 1 a {max_option}")
                time.sleep(1)
            else:
                break
        except:
            print(
                f"\033[91m\033[107m>>>\033[0m Error, el valor ingresado debe ser un número entre 1 y {max_option}"
            )
            time.sleep(1)
    return o
