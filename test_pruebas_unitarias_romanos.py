"""
Para hacer los test, hay que estar dentro del entorno porque así instalamos el pytest y ejecutar en el terminal 
"""
from main import entero_a_romano,RomanNumberError # el * importa todo desde el archivo indicado, si se quiere una función concreta, se importa solo dicha función
import pytest

def test_entero_romano_1994():
    assert entero_a_romano(1994) == "MCMXCIV"

def test_entero_romano_3():
    assert entero_a_romano(3) == "III"

def test_entero_romano_333():
    assert entero_a_romano(333) == "CCCXXXIII"

def test_valor_maximo_3999():
    with pytest.raises(RomanNumberError) as exceptionInfo:
        entero_a_romano(4000)
    assert str(exceptionInfo.value) == "El limite esta entre mayor a 0 y 3999"


