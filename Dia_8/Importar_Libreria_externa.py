#pypi.org pagina oficial de package python
#en mac pip install colored primero se debe brew install tag mas pip install mac-colors
from colored import fg,bg,attr
#importacion de la libreria openpyxl
from openpyxl import *
color = fg(1) + bg(15)
print(color+"hola mundo en color"+ attr(0))

#para trabajar con pdf pip install PyPDF2
#para trabajar con excel pip install xlrd
#para trabajar con pdf pip install pdfminer.six
#para trabajar con excel pip install openpyxl

