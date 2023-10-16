class Entrenador:
    def __init__ (self, codigo, nombre, avistados, pokemones, medallas):
        self.codigo = codigo
        self.nombre = nombre
        self.avistados = avistados
        self.pokemones = pokemones
        self.medallas = medallas

    def capturar(self, pokemon):
        self.pokemones.append(pokemon)
        print("Pokemon capturado")

    def __str__(self):
        return  "Codigo: {}\n" \
                "Nombre: {}\n" \
                "Avistados: {}\n" \
                "Pokemons: {}\n" \
                "Medallas: {}\n" \
                .format(self.codigo, self.nombre, self.avistados, self.pokemones, self.medallas) 