from random import shuffle
#lista inicial
palitos=["-","--","---","----"]

#mezclar palitos
def mezclar (lista):
    shuffle(lista)
    return lista
#pedirle intento
def probar_suerte():
    intento =""
    while intento not in ["1","2","3","4"]:
        intento= input("elige un nuemro del 1 al 4: ")
    return int(intento)
#comprobar intento
def chequear_intento(lista, intento):
    if lista[intento-1]=="-":
        print("a Labar los platos")
    else:
        print("te salvaste")
    print(f"te a tocado {lista[intento-1]}")

#mezclo la lista
palitos_mezclados=mezclar(palitos)
#pedir numero de intentos
seleccion=probar_suerte()
#comprobar intento
chequear_intento(palitos_mezclados,seleccion)