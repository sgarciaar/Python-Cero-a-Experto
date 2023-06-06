import os
import shutil 
#modulo importado
import send2trash

#de esta manera se en que directorio esto parado
print(os.getcwd())
#esto es para crear archivo en caso que no exista
archivo=open('curso.txt','w')
#esto es para escribir en archivo
archivo.write('texto de prueba')
#esto es para cerrar el archivo
archivo.close()
#esro es para listar los archivos por consola
print(os.listdir())
#con shutil podemos mover archivos
shutil.move('curso.txt', '/Users/sebastiangarcia/Desktop/Python/Dia_9')
#elimina todo el arbol de directorios y no van a la papelera
#shutil.rmtree
#y para eliminar archivos pero si enviarlos a la papelera se debe instalar un modulo pip install send2trash
#send2trash.send2trash('/Users/sebastiangarcia/Desktop/Python/Dia_9/curso.txt')
#sirve para recorer la caprteta superior y nos muestre todo lo que hay adentro en forma de generado 
#mietras se lo vaya pidiendo y creara tuplas con los archivod
print(os.walk('/Users/sebastiangarcia/Desktop/Python/'))

ruta='/Users/sebastiangarcia/Desktop/Python/'

for carpeta, sub_carpeta, archivos in os.walk(ruta):
    print(f'en la carpeta: {carpeta}')
    print(f'Las subcarpetas son:')
    for sub in sub_carpeta:
        print(f'{sub}')
    print('los archivos son')
    for arch in archivos:
        print(f'{arch}')

