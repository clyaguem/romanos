"""
1. Crear una función que pase de entero >0 y <4000 a romano
2. Cualquier otra entrada de error
3. Límite 3999

Casos de prueba:
a) 1994 -> MCMXCIV
b) 4000 -> RomanNumberError() el valor debe ser menor a 4000
c) "unacadena" -> RomanNumberError() debe ser un entero

M -> 1000 
D -> 500
C -> 100
L -> 50
X -> 10
V -> 5
I -> 1
"""
diccionario = {1000:"M",500:"D",100:"C",50:"L",10:"X",5:"V",1:"I"}

class RomanNumberError(Exception):
    pass

# a) 1994 -> MCMXCIV
def entero_a_romano():
    return "MCMXCIV"