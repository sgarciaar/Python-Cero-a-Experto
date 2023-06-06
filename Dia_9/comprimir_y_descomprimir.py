import zipfile
import shutil
#esto comprime
mi_zip= zipfile.ZipFile('archivo_comprimido.zip','w')

#archivo que voy a comprimir
mi_zip.write('mi_texto_A.txt')
mi_zip.write('mi_texto_B.txt')

mi_zip.close()

#esto descomprime se pasa el archivo a descomprimir y lo abrira en modo solo lectura
zip_abierto = zipfile.ZipFile('archivo_comprimido.zip','r')
#extrae todos los archivos
zip_abierto.extractall()

#esto se hace con shutil
#comprimir
carpeta_origen='ruta'
#el nombre de la carpeta que quedara el comprimido
archivo_destino='Archivo_comprimido'

shutil.make_archive(archivo_destino,'zip','ruta')

#descomprimir
shutil.unpack_archive('Archivo_comprimido','ruta_destino','zip')