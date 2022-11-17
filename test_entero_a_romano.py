from main import *

def test_entero_a_romano():
    assert entero_a_romano(336) == ['0000','300','30','6']

def test_1():
    assert romano_a_entero("I") == 1

def test_1713():
    assert romano_a_entero("MDCCXIII") == 1713