monedas = 5

while monedas>0:
    print(f"tengo {monedas} monedas")
    monedas = monedas - 1
    #momedas-=1 es lo mismo que la linea de arriba
else: print("No tengo mas monedas")

respuesta ="s"

while  respuesta =="s":
    respuesta = input("quieres seguir (s/n)")
else:
    print("gracias")

#ejercicio con pass

resp="s"
while resp=="s":
#el pass se usa para que podamos ejecutar el codigo sin tomar encuenta el while
    pass
print("hola")

#ejercicio con breack

nombre = input("tu nombre: ")
for letra in nombre:
    if letra == "r":
        break
    print (letra)


