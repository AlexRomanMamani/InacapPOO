from biblioteca.biblioteca import Biblioteca, Libros, Revistas

libro1 = Libros(123, "POO", 2023)
print(libro1)

revista1 = Revistas(456, "Revista 1", 2023, 10)
print(revista1)


libro1.setPrestado(True)
print(libro1)