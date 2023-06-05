#para instalar pylint es pip install pylint
'''
Este es un modulo que imprime algo
'''
#el codigo siempre espera que este en una funcion y 

#antes ,despues de una funcion se esperan 2 lineas en blanco


def una_function():
    numero1=500
    print(numero1)


una_function()

#para verificar si el archivo tiene un error por consola con pylint se ejecuta
#pylint <nombre_archivo.py> -r y
#pylint errores_con_Pylint.py -r y
