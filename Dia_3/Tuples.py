#las tuplas son inmutables ocupan menos espacio de memoria menos que las listas
#y para hacer estructuras inmutables
mi_tupla=(1,2,3,4)
mi_tupla_sin_parentesis= 1,2,3,4
print(type(mi_tupla))
print(type(mi_tupla_sin_parentesis))
tupla2 =(1,'a',2.5)
print(type(tupla2))
#consultar indice
print(tupla2[0])
#con numero negativo cuenta de derecha a izquierda
print(tupla2[-2])
#tuplas anidados
tupla3=(1,2,3,(1,2,3))
print(type(tupla3))
print(tupla3[3][1])
#convertir tupla a lista cast

tupla4= (1,2,3)
tupla4= list(tupla4)
print(type(tupla4))
#convertir lista a tuple
tupla4 = tuple(tupla4)
print(type(tupla4))
#asiganr tuplas a varibles para que esto se cumpla deben haber la misma catidad de items de la tupla que variables a asignar

tupla5=(1,2,3)
x,y,z = tupla5
print(x,y,z)
print(len(tupla5))

tupla6=(1,2,3,4,1,1,1,1)
#count te muestra los valores repetidos que buscas en el parametro de entrada
print(tupla6.count(1))
#consultar en que posision de indice esta el numero que le paso como parametro de entrada
print(tupla6.index(4))
