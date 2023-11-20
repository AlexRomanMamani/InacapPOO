import time

class Disco:
    def __init__(self, codigo, titulo, artista, genero, precio, stock):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__artista = artista
        self.__genero = genero
        self.__precio = precio
        self.__stock = stock
        self.__vendidos = 0
    
    def getCodigo(self):
        return self.__codigo
    def getTitulo(self):
        return self.__titulo
    def getArtista(self):
        return self.__artista
    def getGenero(self):
        return self.__genero
    def getPrecio(self):
        return self.__precio
    def getStock(self):
        return self.__stock
    def getVendidos(self):
        return self.__vendidos
    def setCodigo(self, codigo):
        self.__codigo = codigo
    def setTitulo(self, titulo):
        self.__titulo = titulo
    def setArtista(self, artista):
        self.__artista = artista
    def setGenero(self, genero):
        self.__genero = genero
    def setPrecio(self, precio):
        self.__precio = precio
    def setStock(self, stock):
        self.__stock = stock
    def setVendidos(self, vendidos):
        self.__vendidos = vendidos
    def __str__(self):
        return ("Codigo: {}\n"
                "Titulo: {}\n"
                "Artista: {}\n"
                "Genero: {}\n"
                "Precio: {}\n"
                "Stock: {}\n"
                .format(self.__codigo, self.__titulo, self.__artista, self.__genero, self.__precio, self.__stock))
    
    def vender(self):
        if self.__stock == 0:
            print("No hay stock del disco")
            time.sleep(1)
        self.__stock -= 1
        self.__vendidos += 1
    def reponer(self, cantidad):
        self.__stock += cantidad
    def imprimir(self):
        print(self.__str__())
def creamenu(): 
    return """\n----\033[1m\033[42m\033[37m T I E N D A  B U E N A  M U S I C A \033[0m\033[0m\033[0m----\n
    1 ---- Crear disco
    2 ---- Vender disco
    3 ---- Reponer disco
    4 ---- Imprimir datos de todos los discos
    5 ---- Imprimir datos por disco
    6 ---- Mostrar total de ventas
    7 ---- Salir\n"""

discos = [] 

def crearDisco():
    codigo = input("Ingrese el código del disco: ")
    titulo = input("Ingrese el titulo del disco: ")
    artista = input("Ingrese el artista del disco: ")
    genero = input("Ingrese el genero del disco: ")
    precio = float(input("Ingrese el precio del disco: "))
    stock = int(input("Ingrese la cantidad de discos: "))
    discos.append(Disco(codigo, titulo, artista, genero, precio, stock))
    print("Disco {} creado con éxito!".format(titulo))
    time.sleep(1)
    # Sapo: imprimir discos en lista
    # for disco in discos:
    #     print(disco)

def venderDisco():
    codigo = input("Ingrese el titulo o código del disco a vender: ")
    for disco in discos:
        if disco.getTitulo() == codigo or disco.getCodigo() == codigo:
            disco.vender()
            print("Disco {} vendido con exito!".format(disco.getTitulo()))
            print("Quedan {} discos disponibles.".format(disco.getStock()))
            time.sleep(1)
            break
def reponerDisco():
    codigo = input("Ingrese el titulo o código del disco a reponer: ")
    cantidad = int(input("Ingrese la cantidad de discos a reponer: "))
    for disco in discos:
        if disco.getTitulo() == codigo or disco.getCodigo() == codigo:
            disco.reponer(cantidad)
            print("Se han repuesto {} discos del disco {}.".format(cantidad, codigo))
            print("Nuevo stock: {}".format(disco.getStock()))
            time.sleep(1)
            break
def printAll():
    for disco in discos:
        disco.imprimir()
        time.sleep(1)
def printDisco():
    titulo = input("Ingrese el titulo del disco a imprimir: ")
    for disco in discos:
        if disco.getTitulo() == titulo:
            disco.imprimir()
            time.sleep(1)
def mostrarVendidos():
    longitudes = [7, 20, 20, 10,10]
    formato = "{:<{}}"
    suma = 0
    conteo = 1

    for disco in discos:
        if disco.getVendidos() > 0:
            print(formato.format(conteo, longitudes[0]), formato.format(disco.getTitulo(), longitudes[1]), formato.format(disco.getArtista(), longitudes[2]), formato.format(disco.getPrecio(), longitudes[3]), formato.format(disco.getVendidos(), longitudes[4]))
            suma += disco.getVendidos() * disco.getPrecio()
            conteo += 1
    if suma == 0:
                print("No se han vendido discos aún.")
                time.sleep(1)
    else:
        print("Total: {}".format(suma))
        time.sleep(1)  
