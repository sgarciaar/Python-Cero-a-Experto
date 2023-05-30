class Pajaro:
    #metodo constructor y definimos atributos
    alas= True
    def __init__(self, color,especie):
        self.color=color
        self.especie=especie
    def piar(self):
        #es necesario poner selft dentro de la clase
        print('pio mi color es {}'.format(self.color))
    def volar(self,metros):
        print('voy ',metros,'metros')
        #los metodos pueden llamar a otros metodos
        self.piar()
    def pintat_negro(self):
        #los metodos pueden mutar atributos
        self.color='negro'
        print(f"ahora el pajaro es de color {self.color}")
#metodos de clases
    @classmethod
    def poner_huevos(cls,cantidad):
        print(f"puso {cantidad} huevos")
        #solo puede interactuar con los atributos de clases y no con los de metodo
        cls.alas=False
        print(Pajaro.alas)

    @staticmethod
    def mirar():
        print('miro al cielo')
        


Pajaro.mirar()
Pajaro.poner_huevos(5)
piolin=Pajaro('amarillo','canario')
piolin.pintat_negro()
piolin.volar(100)
piolin.piar()
#podemos modificar algo que corresponde  atoda la clase
piolin.alas=False
print(piolin.alas)