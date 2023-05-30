mi_lista=[1,1,1,1,1,1,1,1,1,1,1]
print(len(mi_lista))

class Objeto:
    pass
mi_objeto=Objeto()


class CD:
    def __init__(self,album,titulo,canciones):
        self.album=album
        self.titulo=titulo
        self.canciones=canciones
    def __str__(self):
    #modifique como quiero que se comporte el metodo str y muestra lo que yo quiera
        return f"album {self.album} del grupo {self.titulo} con {self.canciones} caciones"
    #modificar el comportamiento de len
    def __len__(self):
        return self.canciones
    #modificar el comportamiento de del 
    def __del__(self):
        print(f"se a eliminado el cd")

mi_cd= CD('pink Floyd','the wall',24)
print(mi_cd)
print(len(mi_cd))
#para eliminar mi objeto mi_cd
del mi_cd

