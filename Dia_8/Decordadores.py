#en python todo es un objeto incluso las funciones 


#decorador
def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print("hola")
        funcion(palabra)
        print("adios")
    return otra_funcion


#funcion dentro de funcion
def cambiar_letra(tipo):

    def mayusc(texto):
        print(texto.upper())

    def minusc(texto):
        print(texto.lower())

    #para ver a cual funcion entra hacemos un if
    if tipo == "may":
        return mayusc
    elif tipo == "min":
        return minusc


def mayuscula(texto):
    print(texto.upper())

def minuscula(texto):
    print(texto.lower())

def una_funcion (funcion):
    return funcion

@decorar_saludo
def mayus(texto):
    print(texto.upper())


def minus(texto):
    print(texto.lower())


minus("mensaje con decorador")

minuscula_decorada= decorar_saludo(minus)
minuscula_decorada('Sebastian xd')


#ejecutando funcion dentro de funcion
operacion = cambiar_letra('may')
operacion('palabra')


una_funcion(mayuscula("probando"))


#en python todo es un objeto incluso las funciones 
mi_funcion = mayuscula
#ahora mi_funcion tiene la funcion de mayuscula
mi_funcion('python')

#probando decorador


