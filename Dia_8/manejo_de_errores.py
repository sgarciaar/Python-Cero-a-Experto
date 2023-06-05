def suma():
    n1= int(input("numero 1:"))
    n2= int(input("numero 2:"))
    print(n1+n2)
    print("gracias por sumar")

def pedir_numero():
    while True:
        try:
            numero = int(input("dame un numero"))
        except:
            print("no es un numero")
        else:
            print(f"ingresaste el numero {numero}")
            break
print("gracias")


'''try:
    #Codigo que queremos probar
    suma()
except:
    #Codigo a ejecutar si hay un error
    print("algo no a salido bien")
else:
    #Codigo a ejecutar si no hay un error
    print("hiciste todo bien")

finally:
    #Codigo que se va ejecutar de todos modos
    print("eso fue todo")'''

try:
    #Codigo que queremos probar
    suma()
except TypeError:
    #Codigo a ejecutar si hay un error
    print("estas intentando concatener tipos distintos")
except ValueError:
    #Codigo a ejecutar si hay un error
    print("ese no es un numero")
else:
    #Codigo a ejecutar si no hay un error
    print("hiciste todo bien")

finally:
    #Codigo que se va ejecutar de todos modos
    print("eso fue todo")

