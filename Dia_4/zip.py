#zip une 2 listas y convierte un tuples y luego se castea en lista
nombre =["ana", "hugo","valeria"]
edades=[65,29,43]
ciudades=["lima","peru","mexico"]
#las listas deben tenr el mismo numero de items
combinados = list(zip(nombre,edades,ciudades))
print(combinados)

for nombre, edad ,ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")