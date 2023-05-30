#polumorfismo = muschas formas
class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre+" dice muuuu")

class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre+" dice beeeee")

vaca1=Vaca("aurora")
ovaja1=Oveja("nube")

#vaca1.hablar()
#ovaja1.hablar()
#esto se puede hacer por que comparten el mismo nombre de metodo hablar()
animales=[vaca1,ovaja1]
for animal in animales:
    animal.hablar()

def animal_hablar(animal):
    animal.hablar()

animal_hablar(vaca1)