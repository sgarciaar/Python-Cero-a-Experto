diccionario={'c1':'valor1','c2':'valor2'}
print(type(diccionario))
print(diccionario)
#consultar lo que hay en una de las claves
resultado =diccionario['c1']
print(resultado)
#aguanta todos los tipos de datos y diccionarios dentro de diccionarios y listas
client={'nombre':'juan','apellido':'fuentes','peso':88,'talla':1.76}
consulta=client['apellido']
print(consulta)
#buscar en diccionarios dentro de diccionarios y listas dentro de listas
dic={'c1':55,'c2':[10,20,30],'c3':{'s1':100,'s2':200}}
print(dic['c2'])
print(dic['c2'][1])
print(dic['c3']['s2'])

dic2={'c1':['a','b','c'],'c2':['d','e','f']}
print(dic2['c2'][1].upper())

#agregar item a dic
dic3={1:'a',2:'b'}
dic3[3]='c'
print(dic3)
#sobre escribir un valor existente en diccionario
dic3[2]='B'
print(dic3)
#ver todas las claves dentro de un diccionario
print(dic3.keys())
#ver todas las valores dentro de un diccionario
print(dic3.values())
#ver todos los items dentro de un diccionario
print(dic3.items())