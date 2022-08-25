#1) Con la clase creada en el módulo 7, tener en cuenta diferentes casos en que el código pudiera arrojar error. Por ejemplo, en la creación del objeto recibimos una lista de números enteros pero ¿qué pasa si se envía otro tipo de dato?

import sys
import unittest
sys.path.append(r'/C:/Users/lopez/Documents/Henry/Repos/Python-Prep/08 - Error Handling/herramientas.py')
#usamos este si necesitamos trabajor con un modulo externo se usa este metod appen para decirle 
#al lenguaje que en nuestro espaio de trabajo se añade esta carpeta.
from herramientas import *
import herramientas as h# si hago cambios en herramientas no puedo simplemente volver a importarlo
                        # para eso se usa el importlib lo que hace es volver a cargar el archivo que utilizamos 

"""
ejemplo2=h.Herramientas("hola")

ejemplo1=h.Herramientas(2.4)

h1 = h.Herramientas([2,3,5,6,2])

print("----------------------------------------------------------------")
#2) En la función que hace la conversión de grados, validar que los parámetros enviados sean los esperados, de no serlo, informar cuáles son los valores esperados.
import importlib
importlib.reload(h)#vuelve a cargar el import

h=Herramientas([1,2,3,4,5,6,7])

h.conversion_grados(2,2)


#3) Importar el modulo "unittest" y crear los siguientes casos de pruebas sobre la clase utilizada en el punto 2<br>
#Creacion del objeto incorrecta<br>
#Creacion correcta del objeto<br>
#Metodo valor_modal()<br>
#Se puede usar "raise ValueError()" en la creación de la clase para verificar el error. Investigar sobre esta funcionalidad.
#"raise ValueError()" generamos una exepcion por codigo

import unittest

class testeandomiclase(unittest.TestCase):
    def testcreacionobjeto1(self):
        parametro="dasfsdgfads"
        self.assertRaises(ValueError,Herramientas,parametro)
    
    def testcrearobjeto2(self):
        parametro=[1,2,3,4,5,6,6,6]
        clasetest=Herramientas(parametro)
        self.assertEqual(clasetest.lista,parametro)

    def testmetodo(self):
        listatest=[5,7,11,13]
        testmetodo=Herramientas(listatest)
        resultado= testmetodo.verifica_primo()
        resultadoesperado=[True,True,True,True]
        self.assertEqual(resultado,resultadoesperado)

    def test_valor_modal(self):
        lis = [1,2,1,3]
        h1 = h.Herramientas(lis)
        moda, veces = h1.valor_modal(False)
        moda = [moda]
        moda.append(veces)
        resultado = [1, 2]
        self.assertEqual(moda, resultado)

unittest.main(argv=[''], verbosity=2, exit=False)

#4) Probar una creación incorrecta y visualizar la salida del "raise"

raisetest=Herramientas("dasdfsdfSrgSrgdrgxfgxfgxf")

#6) Agregar casos de pruebas para el método verifica_primos() realizando el cambio en la clase, para que devuelva una lista de True o False en función de que el elemento en la posisicón sea o no primo

class testeandoclase2(unittest.TestCase):
    def testmetodoprimo(self):
        listatest=[5,7,11,12]
        testmetodo=Herramientas(listatest)
        resultado= testmetodo.verifica_primo()
        resultadoesperado=[True,True,True,False]
        self.assertEqual(resultado,resultadoesperado)

unittest.main(argv=[''], verbosity=2, exit=False)
"""
#7) Agregar casos de pruebas para el método conversion_grados()
class testeandoclase3(unittest.TestCase):

    def test_verifica_conversion1(self):
        lista = [2,3,8,10,13]
        h1 = Herramientas(lista)
        grados = h1.conversion_grados('celsius','farenheit')
        grados_esperado = [35.6, 37.4, 46.4, 50.0, 55.4]
        self.assertEqual(grados, grados_esperado)
unittest.main(argv=[''], verbosity=2, exit=False)

#8) Agregar casos de pruebas para el método factorial()
class testeandoclase4(unittest.TestCase):

    def test_verifica_factorial(self):
        lista = [2,3,8,10,13]
        h1 = Herramientas(lista)
        factorial = h1.factorial()
        factorial_esperado = [2, 6, 40320, 3628800, 6227020800]
        self.assertEqual(factorial, factorial_esperado)

#9) Completar el código en las funciones del archivo "checkpoint.py" y probarlo a partir de la ejecución del script "tests.py"