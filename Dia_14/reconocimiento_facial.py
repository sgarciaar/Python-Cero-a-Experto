'''
aplicacion de recnocimiento facial
pip install cmake
pip install dlib
pip install face-recognition
pip install numpy
pip install opencv_python
'''

#from cv2 import cv2
import cv2
import face_recognition as fr


#cargar imagenes
foto_control= fr.load_image_file('Dia_14/FotoA.jpg')
foto_prueba= fr.load_image_file('Dia_14/FotoB.jpg')

#pasar imagenes a RGB
foto_control =cv2.cvtColor(foto_control,cv2.COLOR_BGR2RGB)
foto_prueba =cv2.cvtColor(foto_prueba,cv2.COLOR_BGR2RGB)

#localizar cara control obliga poner el indeice 0
lugar_cara_A = fr.face_locations(foto_control)[0]
#codificamos la cara
cara_codificada_A = fr.face_encodings(foto_control)[0]


#localizar cara control obliga poner el indeice 0
lugar_cara_B = fr.face_locations(foto_prueba)[0]
#codificamos la cara
cara_codificada_B = fr.face_encodings(foto_prueba)[0]

#muesta lugar geolocalozado donde esta la cara
#print(lugar_cara_A)

#mostrar rectangulos

#mostrar rectangulo
cv2.rectangle(foto_control,
            #punto uno del rectangulo
            (lugar_cara_A[3],lugar_cara_A[0]),
            (lugar_cara_A[1],lugar_cara_A[2]),
            #color del rectangulo
            (0,255,0),
            2)
cv2.rectangle(foto_prueba,
            #punto uno del rectangulo
            (lugar_cara_B[3],lugar_cara_B[0]),
            (lugar_cara_B[1],lugar_cara_B[2]),
            #color del rectangulo
            (0,255,0),
            2)


#realizar comparacion el tercer valor es toleracia  0.3 para que las coicidencias se adapten mas 
#resultado= fr.compare_faces([cara_codificada_A],cara_codificada_B,0.3)
#sin el tercer valor
resultado= fr.compare_faces([cara_codificada_A],cara_codificada_B)
#retorna tru o false
#print(resultado)

#medir distancia
#mantener medida de la distacia para comparar la igualdad entre personas en las fotod
distancia = fr.face_distance([cara_codificada_A],cara_codificada_B)
#muestra la distancia en valores si es mallor a 0.6 no se parecen si es menor si se parecen 
#print(distancia)

#mostrar resultado
cv2.putText(foto_prueba,
            f'{resultado} {distancia.round(2)}',
            (50,50),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (0, 255, 0),
            2)





#mostrar imagenes con cv2
cv2.imshow('foto control', foto_control)
cv2.imshow('foto prueba', foto_prueba)

#mantenr el programa abierto
cv2.waitKey(0)
