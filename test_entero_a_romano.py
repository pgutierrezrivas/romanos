import pytest
from main import entero_a_romano,romano_a_entero,RomanNumberError

def test_336():
    assert entero_a_romano(336) == "CCCXXXVI"

def test_2022():
    assert entero_a_romano(2022) == "MMXXII"

def test_1():
    assert romano_a_entero("I") == 1

def test_1713():
    assert romano_a_entero("MDCCXIII") == 1713

def test_romano_a_entero_restar_a_izquierda():
    assert romano_a_entero("IV") == 4

def test_romano_a_entero_no_repetir_mas_de_tres():
    with pytest.raises( RomanNumberError ) as exceptionInfo:
        romano_a_entero("LIIII")    
    assert str(exceptionInfo.value) == "No se puede repetir el valor más de tres veces"
        
def test_romano_a_entero_no_repetir_mas_de_tres_caracteres_especiales():
    with pytest.raises( RomanNumberError ) as exceptionInfo:
        romano_a_entero("DDVVLL")    
    assert str(exceptionInfo.value) == "No se puede repetir estos valores: L,D,V"

def test_romano_a_entero_reglas_de_restas():
    with pytest.raises( RomanNumberError ) as exceptionInfo:
        romano_a_entero("IC")
    assert str(exceptionInfo.value) == "El simbolo romano I solo se puede restar de V y X"

def test_romano_a_entero_VLD_no_se_puede_restar():
    with pytest.raises( RomanNumberError ) as exceptionInfo:
        romano_a_entero("LC")
    assert str(exceptionInfo.value) == "El simbolo romano L no se puede restar"

def test_romano_a_entero_si_hay_repeticiones_no_se_resta():
    with pytest.raises( RomanNumberError ) as exceptionInfo:
        romano_a_entero("IIX")
    assert str(exceptionInfo.value) == "Si hay repeticiones no se resta"

def test_mayor_a_3999():
    with pytest.raises( RomanNumberError ) as exceptionInfo:
        entero_a_romano(4000)    
    assert str(exceptionInfo.value) == "El limite de valor es de 0 a 3999"