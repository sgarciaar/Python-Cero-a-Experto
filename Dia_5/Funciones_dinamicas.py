def chequear_3_cifras(numero):
    return numero in range(100,1000)

resultado= chequear_3_cifras(65)
print(resultado)

def chequear_3_cifras_lista(lista):
    for n in lista:
        if n in range(100,1000):
            return True
        else:
            pass
    return False

resultado2= chequear_3_cifras_lista([55,99,200])
print(type(resultado2))
print(resultado2)

def chequear_3_cifras_lista2(lista2):
    lista_gurdar=[]
    for n in lista2:
        if n in range(100,1000):
            lista_gurdar.append(n)
        else:
            pass
    return lista_gurdar

resultado2= chequear_3_cifras_lista2([555,99,200])
print(type(resultado2))
print(resultado2)