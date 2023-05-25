#tupla
precios_cafe=[("capuchino",2.5),("expresso",3.8),("moka",1.9)]
for elemento in precios_cafe:
    print(elemento)
def cafe_caro(listo_precio):
    precio_mayor=0
    cafe_caro=""

    for cafe,precio in listo_precio:
        if precio>precio_mayor:
            precio_mayor=precio
            cafe_caro=cafe
        else:
            pass
    return(cafe_caro,precio_mayor)

print(cafe_caro(precios_cafe))
cafe,precio =cafe_caro(precios_cafe)
print(f"el cafe mas caro es {cafe} cuyo precio es {precio}")