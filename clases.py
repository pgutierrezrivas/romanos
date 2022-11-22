class Heroe:
    #nombre,poder,apodo son variables de la clase Heroe
    #nombre,poder,apodo son atributos de la clase Heroe
    nombre=""
    poder=""
    apodo=""
    #funcion que inicializa la clase heroe
    #self valor inicial que indica para atributos y funciones que pertenecen a la misma clase
    #se le llama constructor de la clase Heroe
   #self """en lugar de self se puede llamar como yo quiera"""
    def __init__(self,nombre,poder,apodo):
       self.nombre=nombre
       self.poder=poder
       self.apodo=apodo
    
    def saludar(self):
        print("hola como vamos, "+self.nombre)

    #metodo magico devolver una cadena string definida sin tener que llamar a una funcion
    def __str__(self) -> str:
        return f"Heroe: nombre: {self.nombre}, poder:{self.poder}, apodo:{self.apodo}"
    
    #para imprimir sin decir que lo imprima
    def __repr__(self) -> str:
        return f"Heroe: nombre: {self.nombre}, poder:{self.poder}, apodo:{self.apodo}"

#Creamos una variable y lo asignamos a la clase Heroe. Nota: objeto e instancia son lo mismo.
#spiderman es objeto de la clase Heroe
#spiderman es una instancia de la clase Heroe
spiderman = Heroe()
spiderman.nombre="Peter Parker"
spiderman.poder="super fuerza"
spiderman.apodo="Spiderman"

ironman=Heroe()
ironman.nombre="Tony Stark"
ironman.poder="Millonario"
ironman.apodo="Hombre de acero"

print(spiderman.nombre)
print(ironman.nombre)