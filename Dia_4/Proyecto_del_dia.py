from random import randint

intentos = 0
estimado =0
numero_secreto=randint(1,100)

nombre= input("dime tu nombre: ")
print(f"hola, {nombre}, he pensado un numero entre 1 y 100 tiene 8 intentos para adivinar")

while intentos < 8:
    estimado= int(input("cual es el numero?: "))
    intentos+=1
    if estimado not in range (1,101):
        print("tu numero debe ser positivo y estar entre 1 y 100")
    elif estimado < numero_secreto:
        print("el numero es mayor")
    elif estimado > numero_secreto:
        print("el numero es menor")
    else:
        print(f"acertado!!! adivinaste en {intentos} intentos")
        break
if estimado !=numero_secreto:
    print(f"se han agorado los intentos el numero secreto era {numero_secreto}")