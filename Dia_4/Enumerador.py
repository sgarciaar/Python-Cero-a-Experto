#obtener indice de objetos enumerables con enumerate
lista = ["a","b","c"]

for indice, item in enumerate(lista):
   print(indice,item)

for indice, item in enumerate(range(50,55)):
   print(indice,item)

mis_tuples =list(enumerate(lista))
print(mis_tuples)