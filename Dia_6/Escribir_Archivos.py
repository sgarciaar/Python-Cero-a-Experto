#w=escribir y si no existe el archivo lo crea
archivo= open("prueba1.txt","w")
archivo.write("hola\n")
archivo.write("mundo")
archivo.close()

archivo2= open("prueba2.txt","w")
archivo.writelines(['hola','mundo','aca', 'estoy'])
archivo.close()


archivo3= open("prueba3.txt","w")
lista= ['hola','mundo','aca', 'estoy']
for p in lista:
    archivo.writelines(p + '\n')
archivo.close()
#esto es para log y ponemos a
archivo= open("prueba.txt","a")
archivo.write("nueva liena\n")
archivo.close()
