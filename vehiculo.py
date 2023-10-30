class Vehiculo:
    def __init__(self, patente, color, marca, modelo):
        self.__patente = patente,
        self.__color = color,
        self.__marca = marca,
        self.__modelo = modelo
    def __str__(self):
        return "Patente: {}\n" \
                "Color: {}\n" \
                "Marca: {}\n" \
                "Modelo: {}" \
        .format(self.__patente, self.__color, self.__marca, self.__modelo)
    
class Turismo(Vehiculo):
    def __init__(self, patente, color, marca, modelo, tarifa):
        super().__init__(patente, color, marca, modelo)
        self.__tarifa == tarifa

    def __str__(self):
        return "{} \n" \
                "Tarifa: {}" \
                .format(super().__str__(), self.__tarifa)
    
turismo = Turismo("TV123", "Blanco", "Hyundai", "Elantra", 50_000)

print(turismo)