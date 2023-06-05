#las funciones generadoras son recetas y cuidan el espacio de memoria y van creando valores mientras los necesite
#ocupamos yield que es producir
#la generadora es mas eficiente y mas eficiente en memoria

def mi_funcion():
    return 4

def mi_generacion():
    yield 4

#funcion normal
def mi_funcion2():
        lista=[]
        for i in range(1, 5):
             lista.append(i * 10)
        return lista

#funcion con generador
def mi_generador():
    for x in range(1,5):
        yield x * 10

#los yiel no detenen la ejecucion como el return
def mi_generador3():
    x = 1
    yield x

    x+=1
    yield x

    x+=1
    yield x

#ejecutando funciones con for
print(mi_funcion2())
#ehecutamos funcion con generador
gene= mi_generador()
print(next(gene))
print(next(gene))
print(next(gene))



#asi se imprimen las funciones normales
print(mi_funcion())
print(mi_funcion2())

#asi se imprimen los generadores
g= mi_generacion()
print(next(g))


#EJECUTANDO GENERADOR 3

gen3 = mi_generador3()
print(next(gen3))
print(next(gen3))
print(next(gen3))
