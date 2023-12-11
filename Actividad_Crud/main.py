'''Creado por: Alex Mamani'''
'''Version 1.0'''
'''Fecha: 18/05/2021'''

from conexion.conexion import Conexion
from CRUD.CRUD import CRUDUniversidad

try:
    cnx = Conexion()
    DML = CRUDUniversidad(cnx.getConexion())
    while True:
        print("Menú:")
        print("1- ")
        print("2- ")
        print("3- ")
        print("4- ")
        print("5- ")

        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            listar = DML.listar_alumnos()
            print("ASIGNATURA  //  NOMBRE  //  APELLIDO")
            for alumnos in listar:
                print("{}, {}, {}".format(alumnos[0], alumnos[1], alumnos[2]))
        elif opcion == 2:
            listar = DML.listar_asignaturas_mayor_50_horas()
            print("ASIGNATURA  //  HORAS")
            for alumnos in listar:
                print("{}, {}".format(alumnos[0], alumnos[1]))
        elif opcion == 3:
            ...
        elif opcion == 4:
            ...
        elif opcion == 5:
            ...
        elif opcion == 0:
            print("Hasta luego")
            break
        else:
            continue
except Exception as ex:
    print("Main -> {}".format(ex)) # Desde el modulo Main se manejan los errores que puedan ocurrir
    





