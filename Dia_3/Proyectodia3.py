texto = input("ingrese el texto: ")
letras = []

texto.lower()
letras.append(input("ingrese la primera letra: ").lower())
letras.append(input("ingrese la segunda letra: ").lower())
letras.append(input("ingrese la tercera letra: ").lower())

print("Cantidad de letras")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"hemos encontrado la letra '{letras[0]}' repetida {cantidad_letras1} veces")
print(f"hemos encontrado la letra '{letras[1]}' repetida {cantidad_letras2} veces")
print(f"hemos encontrado la letra '{letras[2]}' repetida {cantidad_letras3} veces")

print("Cantidad de palabras")
palabras = texto.split()
print(f"hemos encontrado {len(palabras)} palabras en tu texto")

print("letras de inicio y fin")
letra_inicio= texto[0]
letra_final = texto[-1]

print(f"la letra inicial es '{letra_inicio}' y la letra final es '{letra_final}'")

texto_invertido= palabras.reverse()
texto_invertido =" ".join(palabras)

print(f"si ordenamos tu texto al revez dira '{texto_invertido}'")

print("buscando la palabra python")

buscar_python= 'python' in texto
dic= {True:"si",False:"no"}
print(f"La palabra python {dic[buscar_python]} se encuentra en el texto")


