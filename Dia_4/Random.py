#si remplazamos randint por un * trear todo de la libreria random
from random import *

aleatorio = randint(1,50)
print(aleatorio)

aleatorioDecimal= round(uniform(1,5),1)
print(aleatorioDecimal)

# import random entre 0 y 1 con decimales
random = random()
print(random)

#choice aleatorio con lista de string
colores =["azul","verde","amarillo"]
aleatorio2 = choice(colores)
print(aleatorio2)
#shuffle reodena el oreden de la lista de forma random solo numeron no string
numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)

