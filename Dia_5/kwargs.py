#kwargs significa palabra clave
#a traves de un diccionario
def suma (**kwargs):
    total=0

    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")
        total +=valor
    return total
    print(type(kwargs))

print(suma(x=3, y=2, z=5))
#este es el correcto orden de los parametros de entra del metodo
def prueba (num1,num2,*args,**kwargs):
    print(f"el primer valor rs {num1}")
    print(f"el segundo valor rs {num2}")
    for arg in args:
        print(f"arg es igual a = {arg}")
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")

arg=[100,200,400]
kwargs={'x':'uno','y':'dos','z':3}
#muestra la lista por que los parametros de entrada llevan asteriscos
prueba(15,50,*arg,**kwargs)