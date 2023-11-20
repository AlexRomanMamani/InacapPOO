'''Creado por: Alex Mamani'''
'''Version 1.0'''
'''Fecha: 18/05/2021'''

from conexion.conexion import Conexion
from comandos.comandosDML import ComandosDML

try:
    cnx = Conexion()
    DML = ComandosDML(cnx.getConexion())
    selectPkm = DML.selectPokemon()
    for pokemon in selectPkm:
        print("N° Pokedex: {}".format(pokemon[0]))
        print("Nombre: {}".format(pokemon[1]))
        print("Peso: {}".format(pokemon[2]))
        print("Altura: {}".format(pokemon[3]))
        print("-"*20)
except Exception as ex:
    print("Main -> {}".format(ex)) # Desde el modulo Main se manejan los errores que puedan ocurrir

# 'or 1=1; -- 
# que es? 'or 1=1 -- 
# que es el "?""