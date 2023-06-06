from collections import Counter
from collections import defaultdict
from collections import namedtuple

numeros=[8,6,9,5,4,5,5,8,7,4,5,4,4]
serie=Counter([1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,4])
#con cunter me indica cuantas veces se repiten los numero como si fuera un diccionario
print(Counter(numeros))

print(Counter('Misisipi'))

frase='al pan pan al vino vino'

#al poner frases con split couenta palabras repetifas
print(Counter(frase.split()))
#si pongo el 1 imprimera  el numaro que mas se repite y si pongo 2 me mostrara los 2 mas que se repiten 
print(serie.most_common(1))
#ahora lo casteo en una lista
print(list(serie))

#esto es en caso que no exite la clave solicitada se le asigna la palabra nada
#al no existir esa clave la palabra nada se almacena en el diccionario con la clave que se le otrogo
mi_dic = defaultdict(lambda:'nada')
mi_dic['uno']=['verde']
print(mi_dic['dos'])

print(mi_dic)

#con namedtuple puedo accedeer a los lementos de Persona por el nombre
Persona= namedtuple('Persona',['nombre','altura','peso'])
ariel= Persona('Ariel',1.76,79)
#con namedtuple puedo accedeer a los lementos de Persona por el nombre por ejemplo altura
print(ariel.altura)
#y tambien puedo acceder por el indice
print(ariel[2])






