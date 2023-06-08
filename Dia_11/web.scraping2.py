'''
se deben instalar estas libretias antes de hacer web scraping:
pip install beautifulsoup4
pip install lxml
pip install requests
'''
import bs4
import requests

resultado = requests.get('https://escueladirecta-blog.blogspot.com/2022/11/trucos-de-formato-de-cadenas-en-python.html')
#esta conversion permite navegar buscar entre los elementos de un html
sopa= bs4.BeautifulSoup(resultado.text, 'lxml')
#cuando inicio con un . punto me traigo la clase completa para filrar dejar un espacio y poner otra etiqueta cualquiera p
columna_lateral = sopa.select('.sidebar-container h3')

for h3 in columna_lateral:
    print(h3.get_text())




#columna_lateral = sopa.select('.sidebar-container h3')[0]
#print(columna_lateral)

