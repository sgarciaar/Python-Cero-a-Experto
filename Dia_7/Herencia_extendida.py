class Animal():
    def __init__(self,edad, color):
        self.edad=edad
        self.color=color
    def nacer(self):
        print("Este animal a nacido")
    def hablar(self):
        print("Este animal emite un sonido")


class Pajaro(Animal):

    def __init__(self,edad, color, alturz_vuelo):
         #tambien se puede poner paea heredar todo lo anterior y solo poner las nuevas
        #super().__init__(edad,color)
        self.edad=edad
        self.color= color
        #esta es a nueva
        self.alltura_vuelo=alturz_vuelo
       

    def hablar(self):
        print("pio")
    def volar(self, metros):
        print(f"el pajaro vuela {metros} metros")


piolin = Pajaro(3,'amarillo',60)
#si el metodo se llama igual al de su padre este lo sobre escribe
piolin.hablar()
piolin.volar(3)

mi_animal= Animal(2,'rojo')
