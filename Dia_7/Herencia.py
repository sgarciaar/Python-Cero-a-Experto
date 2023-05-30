class Animal():
    def __init__(self,edad, color):
        self.edad=edad
        self.color=color
    def nacer(selft):
        print("Este animal a nacido")


class Pajaro(Animal):
    pass

#esto me muestra de quien hereda pajaro
print(Pajaro.__base__)
#esto me muestra de quien transmite su herencia
print(Animal.__subclasses__())

piolin= Pajaro(2,'amarillo')
print(piolin.edad)
print(piolin.color)
piolin.nacer()