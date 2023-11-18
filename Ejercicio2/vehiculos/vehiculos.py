class Vehiculo:
    def __init__(self, matricula, marca, modelo, color, tarifa, disponible):
        self.__matricula = matricula
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__tarifa = tarifa
        self.__disponible = True
    
    def __str__(self):
        return ("Matricula: {}\n"
                "Marca: {}\n"
                "Modelo: {}\n"
                "Color: {}\n"
                "Tarifa: {}\n"
                "Disponible: {}\n"
                .format(self.__matricula, self.__narca, self.__modelo, self.__color, self.__tarifa, self.__disponible))

    # Setters
    def setMatricula(self, matricula):
        self.__matricula = matricula
    def setMarca(self, marca):
        self.__marca = marca
    def setModelo(self, modelo):
        self.__modelo = modelo
    def setColor(self, color):
        self.__color = color
    def setTarifa(self, tarifa):
        self.__tarifa = tarifa
    def setDisponible(self, disponible):
        self.__disponible = disponible
    # Getters
    def getMatricula(self):
        return self.__matricula
    def getMarca(self):
        return self.__marca
    def getModelo(self):
        return self.__modelo
    def getColor(self):
        return self.__color
    def getTarifa(self):
        return self.__tarifa
    def getDisponible(self):
        return self.__disponible
    