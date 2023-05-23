#esto d ERROR por que los string son inmutables
#nombre="Carina"
#nombre[0]="k"
#print(nombre)

n1="kari"
n2="na"
print(n1+n2)

#los str se pueden multiplicar

print(n1*10)
#las tre comillas te prmite el salto de espacio con solo eneter
poema="""Mil oequeños peses blancos
      como si hirviera el color
      del agua"""
#como buscar en un print si existe una palabra dentro de una cadena de string y retorna un bool
print("agua" in poema)
#como buscar en un print si NO existe una palabra dentro de una cadena de string y retorna un bool
print("agua" not in  poema)
print(len(poema))