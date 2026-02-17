from main import romano_a_entero,RomanNumberError
import pytest

def test_romano_entero_I():
    assert romano_a_entero("I") == 1

def test_romano_entero_MDCCXIII():
    assert romano_a_entero("MDCCXIII") == 1713

def test_romano_entero_IV():
    assert romano_a_entero("IV") == 4

def test_romano_entero_no_repetir_3_veces01():
    with pytest.raises(RomanNumberError) as exceptionInfo:
        romano_a_entero("IIII")
    assert str(exceptionInfo.value) == "No se puede repetir el mismo valor más de tres veces"

def test_romano_entero_no_repetir_3_veces02():
    with pytest.raises(RomanNumberError) as exceptionInfo:
        romano_a_entero("XXXX")
    assert str(exceptionInfo.value) == "No se puede repetir el mismo valor más de tres veces"    

def test_romano_entero_no_repetir_3_veces03():
    with pytest.raises(RomanNumberError) as exceptionInfo:
        romano_a_entero("CCCC")
    assert str(exceptionInfo.value) == "No se puede repetir el mismo valor más de tres veces"

def test_romano_entero_no_repetir_3_veces04():
    with pytest.raises(RomanNumberError) as exceptionInfo:
        romano_a_entero("MMMM")
    assert str(exceptionInfo.value) == "No se puede repetir el mismo valor más de tres veces"    