class Pokemon():
    """metodo init = metodo constructor"""
    def __init__(self, numero, nombre, peso, altura, tipo, debilidad):
        self.__numero = numero
        self.nombre = nombre
        self.peso = peso
        self.altura = altura
        self.tipo = tipo
        self.debilidad = debilidad
    # De esta forma se declara el numero encapsulado
    def setNumero (self,numero): 
        self.numero = numero
    # De esta forma se obtiene el numero encapsulado
    def getNumero (self, numero):
        return self.numero
#Metodos con __x__ son metodos especiales de python
    def __str__(self):
        return  "Numero: {}\n" \
                "Nombre: {}\n" \
                "Tipo: {}\n" \
                "Debilidad: {}\n" \
                "X: {}\n" \
                "Y: {}" \
                .format(self.nombre, self.nivel, self.tipo, self.debilidad, self.x, self.y)

debilidad = []
numero = int(input("Ingrese el numero del pokemon: "))
nombre = input("Ingrese el nombre del pokemon: ")
peso = float(input("Ingrese el peso del pokemon: "))
altura = float(input("Ingrese la altura del pokemon: "))
tipo = input("Ingrese el tipo del pokemon: ")
for i in range(2):
    debilidad.append(input("Ingrese la debilidad {} del pokemon: ".format(i+1)))
x = int(input("Ingrese la coordenada x del pokemon: "))
y = int(input("Ingrese la coordenada y del pokemon: "))

# INSTANCIAR UN OBJETO
pokemon1 = Pokemon(numero, nombre, peso, altura, tipo, debilidad, x, y)

print(pokemon1)
print(pokemon1.debilidad)
print("Las coordenadas de pokemon1 son: [{}, {}]".format(pokemon1.x, pokemon1.y))

