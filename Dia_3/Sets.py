#los set son inmutablas y se pueden poner []{} y solo muesta objetos unicos
#no tiene orden interno y no se pueden indexar, no puedo poner listas ni diccionarios
#solo admite tuplas y tipos de datos
mi_set=set([1,2,3,4,5])
print(type(mi_set))
print(mi_set)
#otra forma de definir set
otro_set ={1,2,3,4,5}
print(type(otro_set))
print(otro_set)
#set con tupla
set_con_tupla = {1,2,3,4,5,(1,2,3)}
print(type(set_con_tupla))
print(set_con_tupla)
#contando dentro de len
print(len(set_con_tupla))
#buscando dentro de set
print(2 in set_con_tupla)
#union de set con la funcion union
s1={1,2,3}
s2={4,5,6}
s3=s1.union(s2)
print(s3)
#agregar item a set
s1.add(7)
print(s1)
#quitar elementos de un set
#si se elimina un numero que no esta sale erro
s1.remove(1)
print(s1)
#quitando elemto con discrd no sale error si se elimina el elemento que no esta
s1.discard(2)
print(s1)
#con pop vacio se elimina un elemento aleatorio ya que set no tiene orden osea indice
#y se puede almacenar el objeto eliminado en una veriable
objeto_borrado= s1.pop()
print(s1)
print(objeto_borrado)
#la funcion clear vacia nuestri set
s1.clear()
print(s1)
