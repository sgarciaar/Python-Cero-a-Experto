class Pajaro:
    #metodo constructor y definimos atributos
    alas= True
    def __init__(self, color,especie):
        self.color=color
        self.especie=especie
    def piar(self):
        #es necesario poner selft dentro de la clase
        print('pio mi color es {}'.format(self.color))
    def volar(selft,metros):
        print('voy ',metros,'metros')
piolin=Pajaro('amarillo','canario')
piolin.piar()
piolin.volar(500)
print(piolin)