class Pajaro:
    #metodo constructor y definimos atributos
    alas= True
    def __init__(self, color,especie):
       
        self.color=color
        self.especie=especie

mi_pajaro=Pajaro('verde','tukan')
print(mi_pajaro.color)
print(mi_pajaro.especie)
print(Pajaro.alas)
