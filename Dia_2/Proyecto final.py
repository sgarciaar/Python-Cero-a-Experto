nombre = input("ingresa tu nombre ")
ventas = int(input("ingresa tus ventas de este mes "))
comision = round(ventas * 13 / 100 , 2)

print(f"estimado {nombre} tu ganancia en comision es {comision} ")
