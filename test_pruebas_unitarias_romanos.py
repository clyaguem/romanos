"""
Para hacer los test, hay que estar dentro del entorno porque así instalamos el pytest y ejecutar en el terminal 
"""
from main import * # el * importa todo desde el archivo indicado, si se quiere una función concreta, se importa solo dicha función

def test_entero_romano_1994():
    assert entero_a_romano(1994) == "MCMXCIV"
