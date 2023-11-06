from biblioteca.biblioteca import Biblioteca, Libros, Revistas

libro1 = Libros(1, "POO", 2023)
libro2 = Libros(2, "El señor de los anillos", 2023)


revista1 = Revistas(456, "Revista 1", 2023, 10)
revista2 = Revistas(789, "Revista 2", 2023, 20)

libro1.prestarLibro()
libro1.verificarEstado()
libro1.devolverLibro()
libro1.verificarEstado()

print(libro1)
print(libro2)
print(revista1)
print(revista2)