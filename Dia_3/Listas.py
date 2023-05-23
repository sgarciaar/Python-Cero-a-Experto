mi_lista=["a","b","c"]
mi_lista2=["d","e","f"]
print(len(mi_lista))
resultado= mi_lista[0]
#guardar los items de la lista de la posision 0 hasta la 2
resultado= mi_lista[0:2]
print(resultado)
#concatenar listas
mi_lista3= mi_lista+mi_lista2
print(mi_lista3)
#alteraar elementos de una lista
mi_lista3[0]="alfa"
print(mi_lista3)
#agregar item a una lista con append= agregar
mi_lista3.append("g")
print(mi_lista3)
#eliminar elementos de una lista con remove
mi_lista3.remove("g")
print(mi_lista3)
#eliminar elementos de una lista con pop que vacio elimina el ultimo elemento de una lista
mi_lista3.pop()
print(mi_lista3)
#eliminar elementos de una lista con pop pasandole el indice
mi_lista3.pop(0)
print(mi_lista3)
#ahora guardaremos el elemento eliminado
elemeto_borrado = mi_lista3.pop(0)
print(mi_lista3)
print(elemeto_borrado)
#ordenar listas
lista=["g","o","b","m","c"]
lista.sort()
print(lista)
#invertir el orden
lista.reverse()
print(lista)

