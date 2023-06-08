'''
se deben instalar estas libretias antes de hacer web scraping:
pip install beautifulsoup4
pip install lxml
pip install requests
'''
import bs4
import requests

resultado = requests.get('https://escueladirecta-blog.blogspot.com/2022/11/trucos-de-formato-de-cadenas-en-python.html')

#print(type(resultado))
#print(resultado.text)
#esta conversion permite navegar buscar entre los elementos de un html
sopa= bs4.BeautifulSoup(resultado.text, 'lxml')
#retorna una lista con todo lo que busquemos en este caso itlt
print(sopa.select('title'))
print(len(sopa.select('p')))
print(sopa.select('title')[0])
#obtiene el texto sin las etiquetas html en su indice 0
print(sopa.select('title')[0].getText())
#obtiene el texto sin las etiquetas html en su indice 3
parrafo_especial=sopa.select('p')[3].getText()
print(parrafo_especial)


