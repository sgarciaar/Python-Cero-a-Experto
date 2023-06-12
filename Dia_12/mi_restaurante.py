#aplicacion tipo escritorio
from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

operador=''
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadore.delete(0,END)
    visor_calculadore.insert(END, operador)

def borrar ():
    global operador
    operador =''
    visor_calculadore.delete(0,END)

def obtener_resultado():
    global operador
    #eval evalua y suma o resta en el caso necesaro
    resultado=str(eval(operador))
    visor_calculadore.delete(0,END)
    visor_calculadore.insert(0,resultado)
    operador = ''

def revisar_check():
    x= 0
    for c in cuadros_comidas:
        if variable_comida[x].get()==1:
            cuadros_comidas[x].config(state=NORMAL)
            if cuadros_comidas[x].get()=='0':
                cuadros_comidas[x].delete(0,END)
            cuadros_comidas[x].focus()
        else:
            cuadros_comidas[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x+=1
    x= 0
    for c in cuadros_bebidas:
        if variable_bebida[x].get()==1:
            cuadros_bebidas[x].config(state=NORMAL)
            if cuadros_bebidas[x].get() =='0':
                cuadros_bebidas[x].delete(0,END)
            cuadros_bebidas[x].focus()
        else:
            cuadros_bebidas[x].config(state=DISABLED)
            texto_bebida[x].set('0')
        x+=1
    
    x= 0
    for c in cuadros_postres:
        if variable_postre[x].get()==1:
            cuadros_postres[x].config(state=NORMAL)
            if cuadros_postres[x].get()=='0':
                cuadros_postres[x].delete(0,END)
            cuadros_postres[x].focus()
        else:
            cuadros_postres[x].config(state=DISABLED)
            texto_postre[x].set('0')
        x+=1

def total():
    sub_total_comida=0
    p=0
    for cantidad in texto_comida:
        sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[p])
        p+=1

    sub_total_bebida=0
    p=0
    for cantidad in texto_bebida:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebida[p])
        p+=1

    sub_total_postre=0
    p=0
    for cantidad in texto_comida:
        sub_total_postre = sub_total_postre + (float(cantidad.get()) * precios_postres[p])
        p+=1
    
    sub_total= sub_total_comida + sub_total_bebida + sub_total_postre
    impuesto= sub_total* 0.07
    total = sub_total + impuesto

    var_costo_comida.set(f'$ {round(sub_total_comida, 2)}')
    var_costo_bebida.set(f'$ {round(sub_total_bebida, 2)}')
    var_costo_postre.set(f'$ {round(sub_total_postre, 2)}')
    var_subtotal.set(f'$ {round(sub_total,2)}')
    var_impuesto.set(f'$ {round(impuesto,2)}')
    var_total.set(f'$ {round(total,2)}')

def recibo():
    texto_reciblo.delete(1.0, END)
    num_recibo = f'N# - {random.randint(1000,9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day} / {fecha.month} / {fecha.year} - {fecha.hour} : {fecha.minute}'

    texto_reciblo.insert(END, f'datos: {num_recibo}\t\t{fecha_recibo}\n')

    texto_reciblo.insert(END, f'*'* 47 + '\n')
    texto_reciblo.insert(END, 'items Cant Consto Items')
    texto_reciblo.insert(END , f'-' * 54 +'\n')

    x=0
    for comida in texto_comida:
        if comida.get() !='0':
            texto_reciblo.insert(END, f'{lista_comidas[x]}\t\t{comida.get()}\t$ {int(comida.get()) * precios_comida[x]}\n')
        x+=1
    x=0
    for bebida in texto_bebida:
        if bebida.get() !='0':
            texto_reciblo.insert(END, f'{lista_bebidas[x]}\t\t{bebida.get()}\t$ {int(bebida.get()) * precios_bebida[x]}\n')
        x+=1
    x=0
    for postre in texto_postre:
        if postre.get() !='0':
            texto_reciblo.insert(END, f'{lista_postres[x]}\t\t{postre.get()}\t$ {int(postre.get()) * precios_postres[x]}\n')
        x+=1
    texto_reciblo.insert(END , f'-' * 54 +'\n')
    texto_reciblo.insert(END, f'Costo de la comida: \t\t\t {var_costo_comida.get()}\n')
    texto_reciblo.insert(END, f'Costo de la bebida: \t\t\t {var_costo_bebida.get()}\n')
    texto_reciblo.insert(END, f'Costo de la postre: \t\t\t {var_costo_postre.get()}\n')
    texto_reciblo.insert(END , f'-' * 54 +'\n')
    texto_reciblo.insert(END, f'subtotal: \t\t\t {var_subtotal.get()}\n')
    texto_reciblo.insert(END, f'impuestos: \t\t\t {var_impuesto.get()}\n')
    texto_reciblo.insert(END, f'total: \t\t\t {var_total.get()}\n')
    texto_reciblo.insert(END , f'-' * 47 +'\n')
    texto_reciblo.insert(END, 'Lo esperamos pronto')

def guardar():
    info_recibo = texto_reciblo.get(1.0,END)
    archivo = filedialog.asksaveasfile(mode='W',defaultextension= '.txt')
    archivo.write(info_recibo)
    archivo.close()

    messagebox.showinfo('Informacion','Su recibo a sido guardado')

def resetear():
    texto_reciblo.delete(0.1,END)
    for text in texto_comida:
        text.set(0)
    for text in texto_bebida:
        text.set(0)
    for text in texto_postre:
        text.set(0)
    
    for cuadro in cuadros_comidas:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebidas:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postres:
        cuadro.config(state=DISABLED)

    for v in variable_comida:
        v.set(0)
    for v in variable_bebida:
        v.set(0)
    for v in variable_postre:
        v.set(0)
    
    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postre.set('')
    var_subtotal.set('')
    var_impuesto.set('')
    var_total.set('')

#iniciar tkinter
aplicacion = Tk()

#tamaño ventana y apararecer en el punto superior izquierdo iniciada  por el eje y 0 y eje x 0
aplicacion.geometry('1020x630+0+0')

#evitar maximizar en el eje x y eje y
aplicacion.resizable(0,0)

#titulo ventana
aplicacion.title('Mi Restaurante - Sistema de Facturacion')

#color de fondo

aplicacion.config(bg='burlywood')

#panel superior creado con Frame
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
#panel superior se agrega al frame
panel_superior.pack(side= TOP)


#etiqueta titulo
etiqueta_titulo= Label(panel_superior, text='Sistema de Facturacion', fg='azure4',
                    font=('Dosis',58), bg='burlywood',width=27 )

etiqueta_titulo.grid(row=0, column=0)

#panel izquierdo
panel_izquierdo=Frame(aplicacion, bd=1, relief=FLAT, bg='azure4', padx=50)
panel_izquierdo.pack(side=LEFT)

#panel costos
panel_costos= Frame(panel_izquierdo, bd=1, relief=FLAT)
panel_costos.pack(side=BOTTOM)

#panel comidas

panel_comida= LabelFrame(panel_izquierdo,text='Comida',font=('Dosis',19,'bold'),
                        bd=1, relief=FLAT,fg='azure4',bg='burlywood')

panel_comida.pack(side=LEFT)

#panel bebida

panel_bebidas= LabelFrame(panel_izquierdo,text='Bebidas',font=('Dosis',19,'bold'),
                        bd=1, relief=FLAT,fg='azure4',bg='burlywood')

panel_bebidas.pack(side=LEFT)

#panel postre

panel_postres= LabelFrame(panel_izquierdo,text='Postres',font=('Dosis',19,'bold'),
                        bd=1, relief=FLAT,fg='azure4',bg='burlywood')

panel_postres.pack(side=LEFT)

#panel derecha

panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

#panel calculadora
panel_calculadora =Frame(panel_derecha,bd=1, relief=FLAT, bg='burlywood')
panel_calculadora.pack()

#panel calculadora
panel_recibo =Frame(panel_derecha,bd=1, relief=FLAT, bg='burlywood')
panel_recibo.pack()

#panel calculadora
panel_botones =Frame(panel_derecha,bd=1, relief=FLAT, bg='burlywood')
panel_botones.pack()

#lista productos

lista_comidas=['pollo', 'cordero','pizza', 'pizza2', 'merluza', 'salmon','pizza3', 'pizza4']
lista_bebidas=['agua', 'cerveza', 'fanta', 'co2','vino1','vino2','vino3','vino4']
lista_postres=['helado','fruta','flan','pastel','pastel1','pastel2','pastel3','pastel4']


#generear item comida
variable_comida =[]
cuadros_comidas =[]
texto_comida=[]
contador=0

for comida in lista_comidas:
    #crear chackbutton
    variable_comida.append('')
    variable_comida[contador]= IntVar()
    comida = Checkbutton(panel_comida, 
                        text=comida.title(),
                        font=('Dosis',19,'bold'),
                        onvalue=1,
                        offvalue=0,
                        variable=variable_comida[contador],
                        command=revisar_check)                    
    comida.grid(row=contador,column=0, sticky=W)

    #crear cuadros de entrada
    cuadros_comidas.append('')
    texto_comida.append('')
    texto_comida[contador]=StringVar()
    texto_comida[contador].set('0')
    cuadros_comidas[contador]=Entry(panel_comida,
                                    font=('Dosis',18,'bold'),
                                    bd=1,
                                    width=6,
                                    state=DISABLED,
                                    textvariable=texto_comida[contador])
    cuadros_comidas[contador].grid(row=contador,
                                column=1) 
    contador+=1                
#generar item bebidas
variable_bebida =[]
cuadros_bebidas =[]
texto_bebida=[]
contador=0

for bebida in lista_comidas:
    variable_bebida.append('')
    variable_bebida[contador]= IntVar()
    bebida = Checkbutton(panel_bebidas,
                        text=bebida.title(), 
                        font=('Dosis',19,'bold'),
                        onvalue=1,
                        offvalue=0,
                        variable=variable_bebida[contador],
                        command=revisar_check)                    
    bebida.grid(row=contador,
                column=0, 
                sticky=W)
    #crear cuadros de entrada
    cuadros_bebidas.append('')
    texto_bebida.append('')
    texto_bebida[contador]=StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebidas[contador]=Entry(panel_bebidas,
                                    font=('Dosis',18,'bold'),
                                    bd=1,
                                    width=6,
                                    state=DISABLED,
                                    textvariable=texto_bebida[contador])
    cuadros_bebidas[contador].grid(row=contador,
                                column=1) 
    contador+=1

#generar items postrea
variable_postre =[]
cuadros_postres =[]
texto_postre=[]
contador=0

for postre in lista_postres:
    variable_postre.append('')
    variable_postre[contador]= IntVar()
    postre = Checkbutton(panel_postres, 
                        text=postre.title(), 
                        font=('Dosis',19,'bold'),
                        onvalue=1,
                        offvalue=0,
                        variable=variable_postre[contador],
                        command=revisar_check)                    
    postre.grid(row=contador,
                column=0, 
                sticky=W)
    
    #crear cuadros de entrada
    cuadros_postres.append('')
    texto_postre.append('')
    texto_postre[contador]=StringVar()
    texto_postre[contador].set('0')
    cuadros_postres[contador]=Entry(panel_postres,
                                    font=('Dosis',18,'bold'),
                                    bd=1,
                                    width=6,
                                    state=DISABLED,
                                    textvariable=texto_postre[contador])
    cuadros_postres[contador].grid(row=contador,
                                column=1)
    contador+=1




#variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

#etiquetasd e costos y campos de entrada
#comida
etiqueta_costo_comida = Label(panel_costos,
                            text='Costo comida',
                            font=('Dosis',12,'bold'),
                            bg='azure4',
                            fg='white')
etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida = Entry(panel_costos,
                        font=('Dosis',12,'bold'),
                        bd=1,
                        width=10,
                        state='readonly',
                        textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=41)

#bebidas
etiqueta_costo_bebida = Label(panel_costos,
                            text='Costo bebida',
                            font=('Dosis',12,'bold'),
                            bg='azure4',
                            fg='white')
etiqueta_costo_bebida.grid(row=1, column=0)

texto_costo_bebida =Entry(panel_costos,
                        font=('Dosis',12,'bold'),
                        bd=1,
                        width=10,
                        state='readonly',
                        textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx=41)

#postre
etiqueta_costo_postre = Label(panel_costos,
                            text='Costo postre',
                            font=('Dosis',12,'bold'),
                            bg='azure4',
                            fg='white')
etiqueta_costo_postre.grid(row=2, column=0)

texto_costo_postre =Entry(panel_costos,
                        font=('Dosis',12,'bold'),
                        bd=1,
                        width=10,
                        state='readonly',
                        textvariable=var_costo_postre)
texto_costo_postre.grid(row=2, column=1, padx=41)

#subtotal

etiqueta_subtotal = Label(panel_costos,
                            text='SubTotal',
                            font=('Dosis',12,'bold'),
                            bg='azure4',
                            fg='white')
etiqueta_subtotal.grid(row=0, column=2)

texto_subtotal =Entry(panel_costos,
                        font=('Dosis',12,'bold'),
                        bd=1,
                        width=10,
                        state='readonly',
                        textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=41)

#impuesto

etiqueta_impuesto = Label(panel_costos,
                            text='Impuestos',
                            font=('Dosis',12,'bold'),
                            bg='azure4',
                            fg='white')
etiqueta_impuesto.grid(row=1, column=2)

texto_impuesto =Entry(panel_costos,
                        font=('Dosis',12,'bold'),
                        bd=1,
                        width=10,
                        state='readonly',
                        textvariable=var_impuesto)
texto_impuesto.grid(row=1, column=3, padx=41)

#total

etiqueta_total = Label(panel_costos,
                            text='Total',
                            font=('Dosis',12,'bold'),
                            bg='azure4',
                            fg='white')
etiqueta_total.grid(row=2, column=2)

texto_total =Entry(panel_costos,
                        font=('Dosis',12,'bold'),
                        bd=1,
                        width=10,
                        state='readonly',
                        textvariable=var_total)
texto_total.grid(row=2, column=3, padx=41)

#botones y recibo
botones= ['total','recibo','guardar','resetiar']
botones_creados=[]
columnas=0
for boton in botones:
    boton =Button(panel_botones,
                text=boton.title(),
                font=('Dosis',14,'bold'),
                fg='white',
                bg='azure4',
                bd=1,
                width=9)
    
    botones_creados.append(boton)

    boton.grid(row=0,
            column=columnas)
    columnas+=1

botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)


#recibo
texto_reciblo= Text(panel_recibo,
                    font=('Dosis',12,'bold'),
                    bd=1,
                    width=42,
                    height=10)
texto_reciblo.grid(row=0,
                column=0)

#calculadore
visor_calculadore=Entry(panel_calculadora,
                        font=('Dosis',14,'bold'),
                        width=32,
                        bd=1)
visor_calculadore.grid(row=0,
                    column=0,
                    columnspan=4)
botones_calculadora=['7','8','9','+','4','5','6','-',
                    '1','2','3','x','R','B','0','/']

botones_guardados=[]

fila=1
columna=0
for boton in botones_calculadora:
    boton= Button(panel_calculadora,
                text=boton.title(),
                font=('Dosis',16,'bold'),
                fg='white',
                bg='azure4',
                bd=1,
                width=8)
    
    botones_guardados.append(boton)

    boton.grid(row=fila,
            column=columna)
    
    if columna== 3:
        fila +=1

    columna+=1
    if columna ==4:
        columna=0

botones_guardados[0].config(command= lambda :click_boton('7'))
botones_guardados[1].config(command= lambda :click_boton('8'))
botones_guardados[2].config(command= lambda :click_boton('9'))
botones_guardados[3].config(command= lambda :click_boton('+'))
botones_guardados[4].config(command= lambda :click_boton('4'))
botones_guardados[5].config(command= lambda :click_boton('5'))
botones_guardados[6].config(command= lambda :click_boton('6'))
botones_guardados[7].config(command= lambda :click_boton('-'))
botones_guardados[8].config(command= lambda :click_boton('1'))
botones_guardados[9].config(command= lambda :click_boton('2'))
botones_guardados[10].config(command= lambda :click_boton('3'))
botones_guardados[11].config(command= lambda :click_boton('*'))
botones_guardados[12].config(command= obtener_resultado)
botones_guardados[13].config(command= borrar)
botones_guardados[14].config(command= lambda :click_boton('0'))
botones_guardados[15].config(command= lambda :click_boton('/'))




#evitar que la pantalla se cierre
#esto hace que la ventana no finalize por el loop
aplicacion.mainloop()