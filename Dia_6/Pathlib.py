from pathlib import Path, PureWindowsPath
#PureWindowsPath trasnforma cualquier ruta a ruta de windows
carpeta= Path("/Users/sebastiangarcia/Desktop/Python/nueva_ruta/prueba.txt")

#ruta_windows= PureWindowsPath(carpeta)
#con pathlib no se necesita no open ni close
print(carpeta.read_text())
#trae el nombre del archivo
print(carpeta.name)
#vemos la extension del archivo
print(carpeta.suffix)
#trae solo el nombre del archivo
print(carpeta.stem)
#veremos si el archivo existe o no
if not carpeta.exists():
    print("el archivo no existe")
else:
    print("el archivo existe")
