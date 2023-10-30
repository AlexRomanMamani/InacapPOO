class Biblioteca:
    def __init__(self, codigo, titulo, anio):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__anio = anio

    def setcodigo(self, codigo):
        self.__codigo = codigo
    def getcodigo(self):
        return self.__codigo

    def settitulo(self, titulo):
        self.__titulo = titulo
    def gettitulo(self):
        return self.__titulo

    def setAnio(self, anio):
        self.__anio = anio
    def getAnio(self):
        return self.__anio
    
    def __str__(self):
        return  "Codigo: {}\n" \
                "Titulo: {}\n" \
                "Año: {}\n" \
                .format(self.__codigo, self.__titulo, self.__anio)
    
class Libros(Biblioteca):
    def __init__(self, codigo, titulo, anio):
        super().__init__(codigo, titulo, anio)
        self.__prestado = False

    def setPrestado(self, prestado):
        self.__prestado = prestado
    
    def __str__(self):
        return "{}\n" \
        "Prestado: {}\n" \
        .format(super().__str__(), self.__prestado)

class Revistas(Biblioteca):
    def __init__(self, codigo, titulo, anio, numero):
        super().__init__(codigo, titulo, anio,)
        self.__numero = numero
    
    def __str__(self):
        return "{}\n" \
        "Numero: {}\n" \
        .format(super().__str__(), self.__numero)
    