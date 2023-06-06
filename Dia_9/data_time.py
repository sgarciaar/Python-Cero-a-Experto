import datetime
#from datetime import datetime
#from datetime import date

mi_hora= datetime.time(17,35,50,1500)
print(type(mi_hora))
print(mi_hora)
print(mi_hora.min)
mi_dia = datetime.date(2025,10,17)
print(mi_dia)
print(mi_dia.year)
#otro formato de hora
print(mi_dia.ctime())
#imprime el dia de hoy
print(mi_dia.today())

#tabajanfo con from datetime import datetime
#mi_fecha= datetime(2025.5,15,10,15,2500)
#mi_fecha = mi_fecha.replace(month =11)
#print(mi_fecha)

#tabajanfo con from datetime import date
#nacimiento = date(1005,3,5)
#defuncion =date(2095,6,19)
#vida = defuncion -nacimiento
#print(vida)

#tabajanfo con from datetime import datetime
#despierta = datetime(2022,10,5,7,30)
#duerme = datetime(2022,10,5,23,45)
#vigilia = duerme - despierta
#print(vigilia.seconds)