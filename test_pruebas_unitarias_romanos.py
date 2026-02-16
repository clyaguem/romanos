"""
Para hacer los test, hay que estar dentro del entorno porque así instalamos el pytest y ejecutar en el terminal 
"""
from main import entero_a_romano # el * importa todo desde el archivo indicado, si se quiere una función concreta, se importa solo dicha función

def test_entero_romano_1994():
    assert entero_a_romano(1994) == "MCMXCIV"

def test_entero_romano_3():
    assert entero_a_romano(3) == "III"

def test_entero_romano_333():
    assert entero_a_romano(333) == "CCCXXXIII"

