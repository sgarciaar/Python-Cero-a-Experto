#instalamos pygame pip install pygame y luego lo importamos
import pygame
import random
import math
from pygame import mixer

#el init permite inicializarlo
pygame.init()

#creamos la pantalla con la  resolucion 800 ancho por 600 de alto
#Y = alto , X= ancho
pantalla = pygame.display.set_mode((800,600))

#titulo de la pantalla arriba
pygame.display.set_caption('Invacion Espacial')
#cargamos la imagen  de 32px para icon
icono= pygame.image.load('Dia_10/ovni.png')
#mostramos el icono del juego en la ventana arriba solo windows
pygame.display.set_icon(icono)
#imagen como fondo de pantalla
fondo = pygame.image.load('Dia_10/Fondo.jpg')


#agregar musica
mixer.music.load('Dia_10/MusicaFondo.mp3')
#controlamos el volumen
mixer.music.set_volume(0.3)
#se repirata cada vez que termine con el -1
mixer.music.play(-1)

#creamos jugador
img_jugador =pygame.image.load('Dia_10/nave-espacial.png')

#se divide la mitad del ancho que es 400 - el tamaño del jugador 64 = 368 para dejarlo en medio
jugador_x= 368
#aca ponemos el total del alto - los pixeles del tamaño de jugador 600-64
jugador_y= 500

jugador_x_cambio=0

#creamos enemigo
img_enemigo =[]
enemigo_x= []
enemigo_y= []
#cambio de direccion a la derecha
enemigo_x_cambio=[]
enemigo_y_cambio= []
cantidad_enemigos=8

for e in range(cantidad_enemigos):
    #creamos enemigo
    img_enemigo.append(pygame.image.load('Dia_10/fantasma.png'))
    enemigo_x.append( random.randint(0,736))
    enemigo_y.append( random.randint(50,200))
    #cambio de direccion a la derecha
    enemigo_x_cambio.append(1)
    enemigo_y_cambio.append(50)


#creamos bala
img_bala =pygame.image.load('Dia_10/bala.png')
bala_x= 0
bala_y= 500
#cambio de direccion a la derecha
bala_x_cambio=0
#velocidad por pixel
bala_y_cambio= 3
#bala visible o no
bala_visible= False

#puntaje
puntaje =0
fuente= pygame.font.Font('freesansbold.ttf',32)
texto_x= 10
texto_y= 10

#texto final de juego
fuente_final= pygame.font.Font('freesansbold.ttf',40)
def texto_final():
    mi_fuente_final= fuente_final.render("juego terminado",True,(255,255,255))
    pantalla.blit(mi_fuente_final,(60,200))

#funcion mostrar puntaje
def mostrar_puntaje(x,y):
    texto= fuente.render(f'Puntaje: {puntaje}', True, (255,255,255))
    pantalla.blit(texto, (x,y))



#funcion jugador
def jugador(x,y):
    #blit funcion para arrojar por pantalla ubicado en las cordenadas x,y dentro de una tupla
    pantalla.blit(img_jugador,(x,y))

#funcion enemigo
def enemigo(x,y,ene):
    #blit funcion para arrojar por pantalla ubicado en las cordenadas x,y dentro de una tupla
    #se agrega mas 16 y mas 10 para que se corran al centro de la nave
    pantalla.blit(img_enemigo[ene],(x,y))

#funcion bala
def disparar_bala(x,y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala,(x+16,y+10))

def hay_colision(x_1,y_1,x_2,y_2):
    distancia = math.sqrt(math.pow(x_1-x_2,2) + math.pow(y_2-y_1,2))
    if distancia < 27:
        return True
    else:
        return False
    

#haremos que la pantalla quede activa
se_ejecuta= True
#dentro de este loop de hace la programacion para que este escuchando todos los eventos
while se_ejecuta:
    #fill es el relleno de la pantalla color de fondo en  RGB dentro de una tupla
    #pantalla.fill((205,144,228))

    #agregar fonde de pantalla
    pantalla.blit(fondo, (0,0))

    


    #iterar eventos dentro del for ponemos todo lo que se actualice en el juego
    for evento in pygame.event.get():
        #evento para cerrar el progama la x
        if evento.type==pygame.QUIT:
            se_ejecuta=False
        #este evento ve si se presiono alguna tecla cualquiera
        if evento.type == pygame.KEYDOWN:
            #esto valida si se presiona la tecla de las flechas izquierda
            if evento.key == pygame.K_LEFT:
                
                #esto le hace avanzar a la izquierda 0.3 px
                jugador_x_cambio=-1
            #esto valida si se presiona la tecla de las flechas derecha
            if evento.key == pygame.K_RIGHT:
                #esto le hace avanzar a la derecha 0.3 px
                jugador_x_cambio=1
                
            if evento.key == pygame.K_SPACE:
                sonido_bala=mixer.Sound('Dia_10/disparo.mp3')
                sonido_bala.play()
                if bala_visible== False:
                    bala_x= jugador_x
                    disparar_bala(bala_x,bala_y)
        #keyup es cuando suleta la tecla presionada
        if evento.type== pygame.KEYUP:
            if evento.key== pygame.K_LEFT or pygame.K_RIGHT:
                
                #esto hace que al soltar la tecla izquierda o derecha la movilidad sea 0 osea se detenga
                jugador_x_cambio=0
    #movimientos jugador
    #aca se almacena el cambio aplicado a -0.1 o 0.1 dependiendo te la tecla que presiono
    jugador_x+=jugador_x_cambio
    #mantener personaje dentro de los bordes
    #izquierda
    if jugador_x <=0:
        jugador_x =0
    #derecha
    elif jugador_x >= 736:
        jugador_x = 736 
    
    #movimientos enemigo
    for e in range(cantidad_enemigos):

        #fin del juego
        if enemigo_y[e] >500:
            for k in range(cantidad_enemigos):
                enemigo_y[k]=1000
            texto_final()
            break


        enemigo_x[e]+=enemigo_x_cambio[e]

        #mantener enemigo dentro de los bordes
        #izquierda
        if enemigo_x[e] <=0:
            #cambia movimiento hacia la derecha
            enemigo_x_cambio[e] =1
            #enemigo baja al tocar el borde izquierdo
            enemigo_y[e]+=enemigo_y_cambio[e]
        #derecha
        elif enemigo_x[e] >= 736:
            #cambia movimiento hacia la izquiera
            enemigo_x_cambio[e] = -1
            #enemigo baja al tocar el borde derecho
            enemigo_y[e]+=enemigo_y_cambio[e]
        #verificcion de colision
        colision = hay_colision (enemigo_x[e], enemigo_y[e],bala_x, bala_y)
        if colision:
            sonido_colision= mixer.Sound('Dia_10/golpe.mp3')
            sonido_colision.play()
            bala_y =500
            bala_visible= False
            puntaje+=1
            enemigo_x[e]= random.randint(0,736)
            enemigo_y[e]= random.randint(50,200)
        
        #pintamos el enemigo despues de pintar el color de la pantalla
        enemigo(enemigo_x[e],enemigo_y[e],e)


    if bala_y <=-64:
        bala_y=500
        bala_visible=False
    #movimiento bala
    if bala_visible:
        disparar_bala(bala_x,bala_y)
        bala_y-=bala_y_cambio
    
    #pintamos el jugador despues de pintar el color de la pantalla
    jugador(jugador_x,jugador_y)

    mostrar_puntaje(texto_x,texto_y)
    
    #y el update actualiza y muestra el color por pantalla
    pygame.display.update()