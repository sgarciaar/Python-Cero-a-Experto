
mi_texto="este texto largo para fragmentar"

#extrae palabras con indice
extraer_palabra = mi_texto[4:10]
print(extraer_palabra)

caracteres_intercalados= mi_texto[4:10:2]
print(caracteres_intercalados)

abecedario="ABCDEFGHIJKLMNOPQRSTVWXYZ"
fragmento= abecedario[2:10:2]
print(fragmento)
#para invertir la cadena
invertir_fragmento=abecedario[::-1]
print(invertir_fragmento)