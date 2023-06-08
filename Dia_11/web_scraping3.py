'''
se deben instalar estas libretias antes de hacer web scraping:
pip install beautifulsoup4
pip install lxml
pip install requests
'''
import bs4
import requests

resultado = requests.get('https://www.escueladirecta.com/courses')
#esta conversion permite navegar buscar entre los elementos de un html
sopa= bs4.BeautifulSoup(resultado.text, 'lxml')

#extraer imagenes clase con . inicial
imagenes = sopa.select('.course-box-image')[0]['src']
print(imagenes)

imagen_curso_1= requests.get(imagenes)
#archivo binario
#print(imagen_curso_1.content)

#aca creamos el archivo con permiso wb escribir binario
f= open('Dia_11/mi_imagen.jpg', 'wb')
f.write(imagen_curso_1.content)
f.close()