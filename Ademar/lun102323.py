class Humano():
    def __init__(self, edad):
        self.edad = edad
        print("yo soy una parte de un objeto.")
    def hablar(self, mensaje):
        print(self.edad)
        print(mensaje)

# HERENCIA
class IngSistema(Humano):
    def programador(self,lenguaje):
        print("Ustedes estan programando en: ", lenguaje)

pedro = Humano(22)

algo = input("Ingrese mensaje: ")

pedro.hablar(algo)

print(pedro.edad)

juan = IngSistema(22)
juan.programador("Python")
print("Juan tiene : {}".format(juan.edad))
