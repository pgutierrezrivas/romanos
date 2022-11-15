'''
1-Crear una funcion que pase de entero > 0 y < 4000 a romano

2-Cualquier otra entrada debe dar error

Casos de prueba
a) 1994 -> MCMXCIV
b) 4000->RomanNumberError("el valor debe ser menor de 4000")
c)"unacadena" -> RomanNumberErro("debe ser un entero")
d)0-> RomanNumberError("el valor debe ser mayor a cero")
e)-3 ->RomanNumberError("el valor debe ser mayor de cero")
f)4.5 -> RomanNumberError("Debe ser un entero")
'''

class RomanNumberError(Exception):
    pass


u = {
    'I':1, 'II':2, 'III':3,
    'IV':4, 'V':5, 'VI':6,
    'VII':7, 'VIII':8, 'IX':9
}

d = {
    'X':10, 'XX':20, 'XXX':30,
    'XL':40, 'L':50, 'LX':60,
    'LXX':70, 'LXXX':80, 'XC':90
}

c = {
    'C':100,'CC':200,'CCC':300,
    'CD':400,'D':500,'DC':600,
    'DCC':700,'DCCC':800,'CM':900
}

m = {
    'M': 1000, 'MM':2000, 'MMM':3000
}

def entero_a_romano(num):
    lista = []
    num = str(num)

    if len(num)<4:
       num = "{:0>4s}".format(num)
    # for digito in num:
    #        lista.append(digito)
    lista = list(num) 
    for i in range(len(lista)):
        lista[i] = lista[i]+"0"*((len(lista)-1 )-i)
    print(lista)

    return lista




print("funcion en accion",entero_a_romano(336))





