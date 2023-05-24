mi_lista= ['a','b','c']

for letra in mi_lista:
    #aca vemos el indice de cada elemento de la lista
    numero_index = mi_lista.index(letra)
    print(f"letra {numero_index}: {letra}")


lista = ["pablo","laura","fede","luis","julia"]

for nombre in lista:
    if nombre.startswith("l"):
        print(f"{nombre} parte con L")
    else:
        print(f"{nombre} no parten con  una letra L")

lista2 = [1,2,3,4,5]
mi_valor = 0

for numero in lista2:
    mi_valor =mi_valor+ numero
print(mi_valor)

#los string son como arreglos
palabra= 'python'
for letra in palabra:
    print(letra)
#tambien es posible recorrer una lista en el mismo for
for letra in (1,2,3):
    print(letra)

for objeto in [[1,2],[3,4],[5,6]]:
    print(objeto)

for a,b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)

dic ={'clave1':"a",'clave2':"b",'clave3':"c",}
#imprime solo las claves
for clave in dic:
    print(clave)
#imprime los valore
for valore in dic.values():
    print(valore)
for a,b in dic.items():
    print(a)
    print(b)

#suma de pares y impares
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for numero in lista_numeros:
    if numero % 2 == 0:
        suma_pares = suma_pares+numero
    else:
        suma_impares = suma_impares+numero
print(suma_pares)
print(suma_impares)
