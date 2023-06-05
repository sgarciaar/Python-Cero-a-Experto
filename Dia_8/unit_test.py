#unitest no se instala por que viene integrada en python solo se importa
import unittest
import cambia_texto

class Probar_cambia_texto(unittest.TestCase):
    #las funciondes deben empezar con test
    def test_texto_mayuscula(self):
        palabra= 'buen dia'
        resultado = cambia_texto.todo_mayuscula(palabra)
        #assertEqual compara 2 resultados
        self.assertEqual(resultado,'Buen Dia')

if __name__ == '__main__':
    unittest.main()



