from romano_class import NumeroRomano

def test_crear_funcion_entero_a_romano():
    nr = NumeroRomano(35)
    assert nr.representacion == "XXXV"

def test_crear_funcion_romano_a_entero():
    nr = NumeroRomano("CCCXXXIV")
    assert  nr.valor == 334

def test_suma_romanos():
    nr1 = NumeroRomano("XX")
    nr2 = NumeroRomano(30)

    nr3 = nr1 + nr2

    assert isinstance(nr3,NumeroRomano) == True
    assert nr3.valor == 50
    assert nr3.representacion == "L"