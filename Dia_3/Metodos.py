texto="Este es el texto de sebastian"


resultado = texto[2].upper()
resultado = texto.lower()
#por defecto separa por espacios en blanco
resultado = texto.split()
#separa por lo que yo le diga en este cado la letra t
resultado = texto.split("t")


print(resultado)

a="aprender"
b="python"
c="es"
d="genial"
#join une y separa por el espacio en blan que esta al principo
f=" ".join([a,b,c,d])
print(f)

#find busca un caracter dentro de un string  al igual que index

texto2="Este es el texto de sebastian"
#con fiend si la letra no exite retorna -1 a diferencia del retorno de index que devuelve error
rest = texto2.find("s")
print(rest)

texto3="Este es el texto de sebastian"
#con fiend si la letra no exite retorna -1 a diferencia del retorno de index que devuelve error
rest1 = texto3.replace("Este", "Esta")
print(rest1)