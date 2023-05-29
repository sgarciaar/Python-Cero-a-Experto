from pathlib import Path
#crea una path con gerarquia de carpetas
#acepta cadenas como objetos de path
guia = Path("Barcelona", "Sagrada_familia")
#guia = Path(home,"Barcelona", "Sagrada_familia")
#guia = Path("BArcelona", path("Sagrada_familia"))
print(guia)
#ruta absoluta
base =Path.home()
print(base)
guia2= guia.with_name("La_Pedrera")
print(guia2)
#devuelve la capreta antrior y puedo poner cuantos parent sean necesarios
print(guia2.parent)
#enumerar archivos dentro de una carpeta
for txt in guia.glob("*.txt"):
    print(txt)
#metodo glob recursivo agregando a carpetas y sub carpetas
for txt in guia.glob("**/*.txt"):
    print(txt)
guia4=Path("Europa","españa","barselona","madrid","sagrada_familia")
en_auropa= guia4.relative_to(Path("Europa"))
en_espania= guia4.relative_to(Path("Europa","España"))
print(en_auropa)
print(en_espania)