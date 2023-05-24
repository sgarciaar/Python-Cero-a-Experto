palabra="python"

lista=[]

for letra in palabra:
    lista.append(letra)
print(lista)

palabra2="python"
lista2=[letra for letra in palabra2]
print(lista2)

lista3=[numero for  numero in range(0,21)]
print(lista3)

#manipular antes de agregar
lista4=[numero/2 for  numero in range(0,21)]
print(lista4)

#manipular antes de agregar y condicionando
lista5=[n for  n in range(0,21) if n* 2 > 10]
print(lista5)

#manipular antes de agregar y condicionando con else y se pone al principo
lista6=[n if n* 2 > 10 else "no" for  n in range(0,21) ]
print(lista6)

pies= [10,20,30,40,50]
metros =[p*3.281 for p in pies]
print(metros)