import os
#path es un onjeto
from pathlib import Path
#obtener el directorio de trabajo actual getcwd
ruta= os.getcwd()
print(ruta)
# cambiar de directorio para establecer una ruta distinta de trabajo y si no existe la ruta la crea
ruta= os.chdir('/Users/sebastiangarcia/Desktop/Python/nueva_ruta')
archivo = open('prueba.txt')
print(archivo.read())
archivo.close()
#ahora trabajaremos con la ruta ocmpleta
ruta2= "/Users/sebastiangarcia/Desktop/Python/nueva_ruta2/prueba.txt"
elemento= os.path.basename(ruta2)
print(elemento)
ruta3= "/Users/sebastiangarcia/Desktop/Python/nueva_ruta2/prueba.txt"
#aca obtenemos el baseNamePath sin el archivo
elemento= os.path.dirname(ruta3)
#aca obtenrmows el basepath mas el nombre del archivo en una tupla
elemento= os.path.split(ruta3)
print(elemento)
#aca eliminaremos una carpeta
os.rmdir("/Users/sebastiangarcia/Desktop/Python/nueva_ruta2")
#al ponerlo dentro de path permita que la ruta le lea cualquier sistema operativo
carpeta = Path("/Users/sebastiangarcia/Desktop/Python/nueva_ruta3") / "otro_archivo.txt"
mi_archivo = open(carpeta)
print(carpeta.read())
mi_archivo.close()




