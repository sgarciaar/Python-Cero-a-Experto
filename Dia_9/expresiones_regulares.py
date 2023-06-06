import re

texto="Si neceseitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online"

patron = 'ayuda'
busqueda = re.search(patron, texto)
#ubicacion de la palabra
print(busqueda.span())
#comienzo de la palabra
print(busqueda.start())
#fin de la palabra
print(busqueda.end())

#para buscar la cantidad de elementos
busqueda2 = re.findall(patron, texto)
print(len(busqueda2))

for hallazgo in re.finditer(patron, texto):
    print(hallazgo.span())

texto2='llama al 564-525-6588 ya mismo'
#las expresiones regulares parten con r al comienzo del string
patron2= r'\d\d\d-\d\d\d-\d\d\d\d'
#cuantificado es lo mismo de arriba 
patron3= r'\d{3}-\d{3}-\d{4}'

patron4= re.compile(r'(\d{3})-(\d{3})-(\d{4})')

resultado = re.search(patron2, texto2)
#devuelve el obj mas el la ubicacion y el numero
print(resultado)
#devuelve el numero  exacto
print(resultado.group())

#esto devuelve el segundo grupo del valor ya obtenido por la expresion regular
resultado2 = re.search(patron4, texto2)
print(resultado2.group(2))

clave = input('Ingrese Clave: ')
#no  s un numero el primer caracter y 7 caracteres alfanumericos
patron5 = r'\D{1}\w{7}'

chaequear = re.search(patron5, clave)

print(chaequear)

texto3= "no atendemos los lunes por la tarde"

#aca buscamos lunes o martes 
buscar = re.search(r'lunes|martes',texto)

print(buscar)
#el comodin . muestra los valores anteriores para imprimir 
buscar2 = re.search(r'....demos...',texto)
print(buscar2)
#el comodin ^busca la primera lera de la frase si no es un digito
buscar3 = re.search(r'^\D',texto)
print(buscar2)
#el comodin $busca final  de la frase si no es un digito
buscar3 = re.search(r'\D$',texto)
print(buscar2)
#encontrar los que excluyan un espacio vacio
buscar4 = re.findall(r'[^\s]',texto)
print(buscar2)
#esto hace lo mismo que el anterior pero los agrupa en una lista
buscar5 = re.findall(r'[^\s]+',texto)
print(buscar2)

#aca podemos mostrar sin los espacios vacios
print(''.join(buscar5))