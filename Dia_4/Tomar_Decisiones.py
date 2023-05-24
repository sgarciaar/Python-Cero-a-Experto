if 10 > 9 :
    print('10 es mayor que 9')

if True:
    print('Es verdadero')

if 5==2:
    print('5 es igual a 2')
else:
    print('5 es diferente a 2')
#if elif else
mascota = "perro"
if mascota == "gato":
    print("tines un gato")
elif mascota =="perro":
    print("Tines un perro")
else:
    print("no sabes que animal tines")

#if anidados
edad =16
calificacion=9

if edad < 18:
    print("Eres menor de edad")
    if calificacion >=7:
        print("Eres bueno")
    else:
        print("no ERES BUENO")
else:
    print("eres adulto")

edad = 16
tiene_licencia = False
if edad >= 18:
    if tiene_licencia == True:
        print("Puedes conducir")
    else:
        print("No puedes conducir. Necesitas contar con una licencia")
else:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
