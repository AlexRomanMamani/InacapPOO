class Humano():
    def __init__(self):
        self.edad = 30
        print("yo soy una parte de un objeto.")
    def hablar(self, mensaje):
        print(mensaje)
        
pedro = Humano()
algo = input("Ingrese mensaje: ")
pedro.hablar(algo)
print(pedro.edad)