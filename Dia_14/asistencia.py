import cv2
import face_recognition as fr
import os
import numpy
from datetime import datetime

#crear base de datos
ruta = 'Dia_14/Empleados'
mis_imagenes =[]
nombres_empleados =[]
lista_empleados = os.listdir(ruta)
#elimiar primer registro de una lista
del (lista_empleados[0])




#print(lista_empleados)

for nombre in lista_empleados:
    imagen_actual = cv2.imread(f'{ruta}/{nombre}')
    mis_imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0])

print(nombres_empleados)

#codificar imagenes
def codificar(imagenes):
    #crear una lista neuva
    lista_codificada=[]

    #pasar las imagenes a RGB
    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

        #codificar
        codificado = fr.face_encodings(imagen)[0]

        #agregar a la lista
        lista_codificada.append(codificado)

    #devollver lista codificada
    return lista_codificada

#registrar los ingresos
def registrar_los_ingresos(persona):
    f= open('Dia_14/registro.csv','r+')
    lista_datos =f.readline()
    nombre_registros = []
    for linea in lista_datos:
        ingreso= linea.split(',')
        nombre_registros.append(ingreso[0])
    if persona not in nombre_registros:
        ahora = datetime.now()
        #trasndorma el dato en un string
        string_ahora= ahora.strftime('%H:%M%S')
        f.writelines(f'\n {persona}, {string_ahora}')

lista_empleados_codificada= codificar(mis_imagenes)
#print(len(lista_empleados_codificada))

#tomar una imagen de camara web
captura = cv2.VideoCapture(0,cv2.CAP_DSHOW)






#leer imagen de la camara
exito, imagen = captura.read()

if not exito:
    print("no se pudo tomar la captura")
else:
    #rreconocer cara en caaptura
    cara_captura = fr.face_locations(imagen)
    #codificar cara capturada
    cara_captura_codificada= fr.face_encodings(imagen, cara_captura)

    #buscar coincidencias
    for caracodif, caraubic in zip(cara_captura_codificada, cara_captura):
        coincidencia = fr.compare_faces(lista_empleados,caracodif)
        distancias = fr.face_distance(lista_empleados_codificada,caracodif)

        indice_coincidencia= numpy.argmin(distancias)

        #mostrar coincidencia
        if distancias[indice_coincidencia]> 0.6:
            print("no coincide con ninguno de nuestros empleados")

        else:
            #buscar el nombre del empleado encontrado
            nombre = nombres_empleados[indice_coincidencia]

            y1,x2,y2,x1 = caraubic
            cv2.rectangle(imagen, (x1, y1),(x2, y2),(0,255,0),2)
            cv2.rectangle(imagen, (x1, y2 -35), (x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(imagen, nombre, (x1+ 6, y2 -6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)

            registrar_los_ingresos(nombre)

            #mostrar la imagen btenida
            cv2.imshow('imagen web', imagen)

            #mantener ventana abierta
            cv2.waitKey(0)



