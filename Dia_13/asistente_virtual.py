'''
instalamos 
pip install pyttsx3 (esto nos sirve para que podamos hablar con el asistente y el con nosotros)
pip install SpeechRecognition (permite reconocer el sonido de la voz y convertirlo en texto)
pip install pywhatkit (permite que nuestro sistema abra sitios como youtube, wikipedia etc)
pip install yfinance (yahoo finance nos conceta con el mercado financiero)
pip install pyjokes (permite que nuesgtro asistente nos pueda contar chistes)
pip install pipwin
pipwin install PyAudio
pip install flask
'''
#para mac
from Foundation import *

import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

#elegimos la voz por el id
id1=''
id2=''
id3=''
id4=''

#escuchar nuestra voz y trasnformarlo en texto
def transformar_audio_en_text():
    #almacenar el reconocedor en una variable
    r= sr.Recognizer()

    #configurar microfono
    with sr.Microphone() as origen:
        #tiempo de espera en activar microfono y escuchar
        r.pause_threshold=0.8

        #informar que comenzo la grabacion
        print("Escuchando...")

        #guardar lo que escuche como audio
        audio = r.listen(origen)

        print("1")

        try:
            # buscar en google lo que alla escuchado
            pedido = r.recognize_google(audio, language="es-ES")
            
            #prueba de que pudo ingrsar 
            print("dijiste: " + pedido)

            #devolver pedido
            return pedido
        except sr.UnknownValueError:
            #prueba de que no comprendio el audio
            print("Ups... no te entendi")

            return "sigo esperando"
        
        #en caso de que no pudo resolver el pedido
        except sr.RequestError:
            #prueba de que no comprendio el audio
            print("Ups... no hay servicio")
            print(sr.RequestError)
            return "sigo esperando"
        # error inesperado
        except:
            print("Ups... algo a salido mal")
            print(sr.RequestError)

            return "sigo esperando"

#probar si el asistente escucha nuestra voz
#transformar_audio_en_text()

def hablar (mensaje):
    #encender el motor de pyttsx3
    engine = pyttsx3.init()

    #seleccionamos la voz
    #engine =pyttsx3.setProperty('voice', id1)
    #pronunciar mensaje
    engine.say(mensaje)
    #ejecutar mensaje y esperar
    engine.runAndWait()

#hablar("hola Sebastian, espero que tengas un buen dia")


#ver la cantitad de voces que tiene pyttsx3
'''engine = pyttsx3.init()
for voz in engine.getProperty('voice'):
    print(voz)'''



#informar el dia de la semana
def pedir_dia():
    #crear variables con datos de hoy
    dia = datetime.date.today()
    #crear variable para el dia de la semana
    dia_semana = dia.weekday()

    #diccionario con los nombre de los dias
    calendario = {0: 'Lunes',
                1: 'Martes',
                2: 'Miércoles',
                3: 'Jueves',
                4: 'Viernes',
                5: 'Sábado',
                6: 'Domingo'}
    
    #decir el dia de la semana
    hablar(f'Hoy es {calendario[dia_semana]}')

#pedir_dia()
#pedir hora
def pedir_hora():
    #crear una variable con datos de la hora
    hora = datetime.datetime.now()
    
    #decir la hora actual
    hablar(f"en este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos")

#pedir_hora()

#funcion saludo inicial
def saludo_inicial():
    #crear variable con datos de hora
    hora= datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas Noches'
    elif 6 <=   hora.hour <12:
        momento = 'Buen Día'
    else:
        momento = 'Buenas Tardes'

    #decir slaudo
    hablar(f"{momento}, soy JARVIS, tu asistente personal. Por favor dime en que te puedo ayudar ")

#saludo_inicial()
#funcion central del asistente
def pedir_cosas():
        saludo_inicial()

        #variable de corte
        comenzar= True
        #loop centrar
        while comenzar:
            #activar el micro y guardar pedido en un string
            pedido =  transformar_audio_en_text().lower()

            if 'abrir youtube' in pedido:
                hablar ('Con gusto, estoy abriendo youTube')
                webbrowser.open('https://www.youtube.com')
                continue
            elif 'abrir navegador' in pedido:
                hablar("Abriéndo  navegador")
                webbrowser.open('https://wwww.google.cl')
                continue
            elif 'qué día es hoy' in pedido:
                pedir_dia()
                continue
            elif 'qué hora es' in pedido:
                pedir_hora()
                continue
            elif 'busca en wikipedia' in pedido:
                hablar('Buscando eso en wikipedia')
                pedido = pedido.replace('busca en wikipedia','')
                wikipedia.set_lang('es')
                #se guardara en resultado el resumen summary del pedito del primer parrafo  sentences 1
                resultado = wikipedia.summary(pedido, sentences = 1)
                hablar('Wikipedia dice lo siguiente:')
                hablar(resultado)
                continue
            elif 'busca en internet' in pedido:
                hablar('Buscando eso en internet')
                pedido = pedido.replace('busca en internet','')
                pywhatkit.search(pedido)
                hablar('Esto es lo que he encontrado')
                continue
            elif 'reproducir en youtube' in pedido:
                hablar('Buena idea, ya comienzo a reproducirlo')
                pywhatkit.playonyt(pedido)
                continue
            elif 'dime un chiste' in pedido:
                hablar(pyjokes.get_joke('es'))
                continue
            elif 'precio de las acciones' in pedido:
                accion = pedido.split('de')[-1].strip()
                cartera = {'apple':'APPL',
                    'amazon':'AMZN',
                    'google':'GOOGL'}
                try:
                    accion_buscada = cartera[accion]
                    accion_buscada = yf.Ticker(accion_buscada)
                    precio_actual = accion_buscada.info['regularMarketPrice']
                    hablar(f'La encontré, el precio de {accion} es {precio_actual}')
                    continue
                except:
                    hablar("Perdón pero no la he encontrado")
                    continue
            elif 'adiós' in pedido:
                hablar("Me voy a descansar, cualquier cosa me avisas")
                break

pedir_cosas()
            