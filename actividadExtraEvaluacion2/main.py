import time
from discos.discos import Disco
import discos.discos as d



while True:
    
    print(d.creamenu())
    try:
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            d.crearDisco()
        elif opcion == 2:
            d.venderDisco()
        elif opcion == 3:
            d.reponerDisco()
        elif opcion == 4:
            d.printAll()
        elif opcion == 5:
            d.printDisco()
        elif opcion == 6:
            d.mostrarVendidos()
        elif opcion == 7:
            print("Saliendo...")
            break
    except ValueError:
        input(
            ">>> Se ha encontrado un error. Presione Enter para volver al Menu Principal..."
        )