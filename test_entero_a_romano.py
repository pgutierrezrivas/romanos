import pytest
from main import *

def test_entero_a_romano():
    assert entero_a_romano(336) == ['0000','300','30','6']

def test_1():
    assert romano_a_entero("I") == 1

def test_1713():
    assert romano_a_entero("MDCCXIII") == 1713

def test_romano_a_entero_no_repetir_mas_de_tres():
    with pytest.raises( RomanNumberError) as exceptionInfo:
        romano_a_entero("LIIII")
    assert str(exceptionInfo.value) == "No se puede repetir el valor más de tres veces"