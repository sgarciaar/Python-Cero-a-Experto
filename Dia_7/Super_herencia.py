class Padre:
    def hablar(self):
        print("hola")

class Madre:
    def reir(self):
        print("ja ja ja")
    def hablar(self):
        print("que tal")

class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass


mi_nieto= Nieto()
mi_nieto.hablar()
#el metodo reir dira hola por que hijo primero heredo de Padre y luego de Madre por el orden de busqueda hacia arriba
mi_nieto.reir()
#mro significa method orden resolution y te muestra el orden en que busca el metodo para usar
print(Nieto.__mro__)