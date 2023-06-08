'''
se deben instalar estas libretias antes de hacer web scraping:
pip install beautifulsoup4
pip install lxml
pip install requests
'''
import bs4
import requests

url_base = "http://books.toscrape.com/catalogue/page-{}.html"

resultado = requests.get(url_base.format('1'))
sopa= bs4.BeautifulSoup(resultado.text, 'lxml')

libros = sopa.select('.product_pod')
#cuanhay un espacio vacio se reemplaa con un . punto
#ejemplo = libros[0].select('.star-rating.Four')

ejemplo = libros[0].select('a')[1]['title']

print(ejemplo)

#for n in range(1,11):
#    print(url_base.format(n))

#resultado = requests.get('http://books.toscrape.com/')
#esta conversion permite navegar buscar entre los elementos de un html
#sopa= bs4.BeautifulSoup(resultado.text, 'lxml')