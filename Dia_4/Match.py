#coincidencia de patrones estructurales esto es como un switch case dedes la version 3.1 en pyton
serie ="n-02"
match serie:
    case "n-01":
        print("n-01")
    case "n-02":
        print("n-02")
    case "n-03":
        print("n-03")
    case "n-04":
        print("n-04")

cliente = {"nombre":"federico","edad":25,"ocupacion":"instructor"}
pelicula={"titulo":"matrix","ficha_tecnica":{"protagonista":"Keanu Reeves","director":"lana y Lilly Wachoski"}}

elementos =[cliente, pelicula, "libro"]


for e in elementos:
    match e:
        case {"nombre":nombre,"edad":edad,"ocupacion":ocupacion}:
            print("es un cliente")
            print(nombre, edad, ocupacion)
        case {"titulo":titulo, "ficha_tecnica":{"protagonista":protagonista,"director":director}}:
            print("es una pelicula")
            print(titulo,protagonista,director)
            #el guion bajo es un valor por defecto
        case _:
            print("no se que es esto")



