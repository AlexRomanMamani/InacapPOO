class Pokemon:
    def volver(self):
        self.x = 0
        self.y = 0

    def mover(self,x,y):
        self.x=x
        self.y=y

charmander = Pokemon()
pikachu = Pokemon()

charmander.tipo = "Fuego"
pikachu.nivel = 100

charmander.volver()
print("Charmander: [{},{}]".format(charmander.x, charmander.y))
charmander.mover(4,6)
print("Charmander: [{},{}]".format(charmander.x, charmander.y))



