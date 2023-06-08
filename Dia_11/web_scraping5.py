'''
se deben instalar estas libretias antes de hacer web scraping:
pip install beautifulsoup4
pip install lxml
pip install requests
'''
import bs4
import requests

url_base = "http://books.toscrape.com/catalogue/page-{}.html"

#listo titulos con 4 o 5 estellas
titulos_rating_alto= []


#iterar paginas
for paginas in range(1,51):
    #crear sopa por pagina
    url_pagina = url_base.format(paginas)
    resultado= requests.get(url_pagina)
    sopa= bs4.BeautifulSoup(resultado.text, 'lxml')

    #seleccionar datos de los libros
    libros = sopa.select('.product_pod')

    #iterar en los libros
    for libro in libros:

        #chequear que tengan 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) !=0 or len(libro.select('.star-rating.Five')):
            #guardar titulo de libro en variable
            titulo_libro = libro.select('a')[1]['title']


            #agregar libro a lista
            titulos_rating_alto.append(titulo_libro)

#ver libros de 4 y 5 estrellas en consola
for t in titulos_rating_alto:
    print(t)


