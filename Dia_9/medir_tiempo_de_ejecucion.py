#aca mediremos cual de las funciones es mas rapida con marcas de tiempo usando el modulo time

import time
import timeit

def prueba_for(numero):
    lista=[]
    for num in range(1,numero+1):
        lista.append(num)
    return lista

def prueba_while(numero):
    lista=[]
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador +=1
    return lista

#aca usamos las marcas de tiempo de inicio entre funcion
inicio = time.time()
prueba_for(1000000)
#aca usamos las marcas de tiempo de final entre funcion
final = time.time()
#y esto nos imprimira cuanto tiempo duro la ejecucion de la funcion 
print(final - inicio)

inicio = time.time()
prueba_while(1000000)
final = time.time()
print(final - inicio)


declaracion = '''
prueba_for(10)
'''

mi_setup='''
def prueba_for(numero):
    lista=[]
    for num in range(1,numero+1):
        lista.append(num)
    return lista
'''
#a esta funcion le pasamos la declaracion , mi setap, y las veces que quiero que se reputa en la 
#en la variable number
duracion=timeit.timeit(declaracion,mi_setup, number=1000000)
print(duracion)

declaracion2='''
prueba_while(10)
'''
mi_setup2='''
def prueba_while(numero):
    lista=[]
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador +=1
    return lista
'''
#a esta funcion le pasamos la declaracion , mi setap, y las veces que quiero que se reputa en la 
#en la variable number
duracion2=timeit.timeit(declaracion2,mi_setup2, number=1000000)
print(duracion2)