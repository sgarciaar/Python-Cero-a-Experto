#EL archivo debe estar en la raiz del proyecto para abrirlo de esta manera y aca no modificamos el archivo
mi_archivo = open('prueba.txt')
print(mi_archivo.read())
mi_archivo.close()


mi_archivo3= open('prueba.txt')
#imprime una linea y si la pego n veces se ve ene lineas
una_linea = mi_archivo3.readline()
print(una_linea.upper())
#imprime una linea y si la pego n veces se ve ene lineas
una_linea = mi_archivo3.readline()
#rstrip quita el salto de linea
print(una_linea.rstrip())
#imprime una linea y si la pego n veces se ve ene lineas
una_linea = mi_archivo3.readline()
print(una_linea)
mi_archivo3.close()

mi_archivo4= open('prueba.txt')
#siempre es necesario cerrar el archivo al final de la ejecucion 
for l in mi_archivo4:
    print("Aqui dice: "+l)
mi_archivo4.close()



mi_archivo2 = open('prueba.txt')
#crea una lista 
todas = mi_archivo2.readlines()
print(todas)
mi_archivo2.close()


