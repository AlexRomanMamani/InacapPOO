class Pokemon():
    """metodo init= metodo constructor"""
    def __init__(self, numero, nombre, peso, altura, tipo, debilidad):
        self.numero = numero
        self.nombre = nombre
        self.peso = peso
        self.altura = altura
        self.tipo = tipo
        self.debilidad = debilidad
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

nombre = input("Ingrese el nombre del pokemon: ")
nivel = int(input("Ingrese el nivel del pokemon: "))
tipo = input("Ingrese el tipo del pokemon: ")
for i in range(2):
    debilidad.append(input("Ingrese la debilidad {} del pokemon: ".format(i+1)))
x = int(input("Ingrese la coordenada x del pokemon: "))
y = int(input("Ingrese la coordenada y del pokemon: "))

charmander = Pokemon(nombre, nivel, tipo, debilidad, x, y)

print(charmander)
print(charmander.debilidad)
print("Las coordenadas de Charmander son: [{}, {}]".format(charmander.x, charmander.y))

