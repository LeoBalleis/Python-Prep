#1) Crear la clase vehículo que contenga los atributos:<br>
##Color<br>
##Si es moto, auto, camioneta ó camión<br>
#Cilindrada del motor

from math import factorial


class vehiculo:
    def __init__(self ,color, tipo, cilindrada):
        self.color=color
        self.tipo=tipo
        self.cilindrada=cilindrada
print("---------------------------------------------------------------------------------")

#2) A la clase Vehiculo creada en el punto 1, agregar los siguientes métodos:<br>
#Acelerar<br>
#Frenar<br>
#Doblar<br>


class vehiculo:
    def __init__(self ,color, tipo, cilindrada):
        self.color=color
        self.tipo=tipo
        self.cilindrada=cilindrada
        self.velocidad= 0
        self.direccion=0

    def Acelerar(self,velocidad):
        self.velocidad+=velocidad

    def Frenar (self,velocidad):
        self.velocidad-=velocidad

    def Doblar (self,grados):
        self.direccion+=grados
print("---------------------------------------------------------------------------------")
      
#3) Instanciar 3 objetos de la clase vehículo y ejecutar sus métodos, probar luego el resultado

a1=vehiculo("rojo","moto",1)
a2=vehiculo("rojo","auto",2)
a3=vehiculo("rojo","camion",4)

a1.Acelerar(100)
a2.Acelerar(80)
a3.Doblar(60)

print(a1.velocidad)
print(a2.velocidad)
print(a3.direccion)
print("---------------------------------------------------------------------------------")
#4) Agregar a la clase Vehiculo, un método que muestre su estado, es decir, a que velocidad se encuentra y su dirección. Y otro método que muestre color, tipo y cilindrada


class vehiculo:
    def __init__(self, color, tipo, cilindrada):
        self.color = color
        self.tipo = tipo
        self.cilindrada = cilindrada
        self.velocidad = 0
        self.direccion = 0

    def Acelerar(self, vel):
        self.velocidad += vel

    def Frenar(self, vel):
        self.velocidad -= vel
    
    def Doblar(self, grados):
        self.direccion += grados

    def Estado(self):
        print('Velocidad:', self.velocidad, '- Dirección:', self.direccion)

    def Detalle(self):
        print('Soy', self.tipo, 'de color', self.color, 'y mi cilindrada es de', self.cilindrada, 'litros')


a1=vehiculo("verde","auto",2)
a1.Acelerar(20)
a1.Doblar(30)
a1.Estado()
a1.Detalle()


print("---------------------------------------------------------------------------------")

#5) Crear una clase que permita utilizar las funciones creadas en la práctica del módulo 6<br>
#Verificar Primo<br>
#Valor modal<br>
#Conversión grados<br>
#Factorial<br>



class multifuncion:
    def __init__(self) -> None:
        pass
    
    def primo(self,numero):
        x =1
        c=0
        while x <= numero:
            if numero % x ==0:
             c+=1
            x+=1
        if c==2:
            return True
        else:
            return False
    
    def cuentalistas(self,lista,trueofalse):
        if trueofalse== True:
            nuevodiccrepes=dict(zip(lista,map(lambda x: lista.count(x),lista)))
            return (f"el que mas se repite es el {max(nuevodiccrepes, key=nuevodiccrepes.get),nuevodiccrepes[max(nuevodiccrepes, key=nuevodiccrepes.get)]} veces") 
        else:
            nuevodiccrepes=dict(zip(lista,map(lambda x: lista.count(x),lista)))
            return (f" el que menos se repite es {min(nuevodiccrepes, key=nuevodiccrepes.get),nuevodiccrepes[min(nuevodiccrepes, key=nuevodiccrepes.get)]} veces")
    
    def conversion_grados(self,valor, origen, destino):
        if (origen == 'celsius'):
            if (destino == 'celsius'):
                valor_destino = valor
            elif (destino == 'farenheit'):
                valor_destino = (valor * 9 / 5) + 32
            elif (destino == 'kelvin'):
                valor_destino = valor + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif (origen == 'farenheit'):
            if (destino == 'celsius'):
                valor_destino = (valor - 32) * 5 / 9
            elif (destino == 'farenheit'):
                valor_destino = valor
            elif (destino == 'kelvin'):
                valor_destino = ((valor - 32) * 5 / 9) + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif (origen == 'kelvin'):
            if (destino == 'celsius'):
                valor_destino = valor - 273.15
            elif (destino == 'farenheit'):
                valor_destino = ((valor - 273.15) * 9 / 5) + 32
            elif (destino == 'kelvin'):
                valor_destino = valor
            else:
                print('Parámetro de Destino incorrecto')
        else:
            print('Parámetro de Origen incorrecto')
        return valor_destino
        
    def factorial(self,numero):
        if(type(numero) != int):
            return 'El numero debe ser un entero'
        if(numero < 0):
            return 'El numero debe ser positivo'
        if (numero > 1):
            numero = numero *factorial(numero - 1)
        return numero


m= multifuncion()
    
print("---------------------------------------------------------------------------------")

#6) Probar las funciones incorporadas en la clase del punto 5
listareper=[1,2,3,4,4,4,4,5]
print(m.primo(3))
print(m.cuentalistas(listareper,True))
print(m.cuentalistas(listareper,False))
print(m.conversion_grados(20,"celsius",'farenheit'))
print(m.factorial(3))

#7) Es necesario que la clase creada en el punto 5 contenga una lista, sobre la cual se aplquen las funciones incorporadas
class Herramientas:
    def __init__(self, lista_numeros):
        self.lista = lista_numeros

    def verifica_primo(self):
        for i in self.lista:
            if (self.__verifica_primo(i)):
                print('El elemento', i, 'SI es un numero primo')
            else:
                print('El elemento', i, 'NO es un numero primo')

    def conversion_grados(self, origen, destino):
        for i in self.lista:
            print(i, 'grados', origen, 'son', self.__conversion_grados(i, origen, destino),'grados',destino)
    
    def factorial(self):
        for i in self.lista:
            print('El factorial de ', i, 'es', self.__factorial(i))

    def __verifica_primo(self, nro):
        es_primo = True
        for i in range(2, nro):
            if nro % i == 0:
                es_primo = False
                break
        return es_primo

    def valor_modal(self, menor):
        lista_unicos = []
        lista_repeticiones = []
        if len(self.lista) == 0:
            return None
        if (menor):
            self.lista.sort()
        else:
            self.lista.sort(reverse=True)
        for elemento in self.lista:
            if elemento in lista_unicos:
                i = lista_unicos.index(elemento)
                lista_repeticiones[i] += 1
            else:
                lista_unicos.append(elemento)
                lista_repeticiones.append(1)
        moda = lista_unicos[0]
        maximo = lista_repeticiones[0]
        for i, elemento in enumerate(lista_unicos):
            if lista_repeticiones[i] > maximo:
                moda = lista_unicos[i]
                maximo = lista_repeticiones[i]
        return moda, maximo

    def __conversion_grados(self, valor, origen, destino):
        valor_destino = None
        if (origen == 'celsius'):
            if (destino == 'celsius'):
                valor_destino = valor
            elif (destino == 'farenheit'):
                valor_destino = (valor * 9 / 5) + 32
            elif (destino == 'kelvin'):
                valor_destino = valor + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif (origen == 'farenheit'):
            if (destino == 'celsius'):
                valor_destino = (valor - 32) * 5 / 9
            elif (destino == 'farenheit'):
                valor_destino = valor
            elif (destino == 'kelvin'):
                valor_destino = ((valor - 32) * 5 / 9) + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif (origen == 'kelvin'):
            if (destino == 'celsius'):
                valor_destino = valor - 273.15
            elif (destino == 'farenheit'):
                valor_destino = ((valor - 273.15) * 9 / 5) + 32
            elif (destino == 'kelvin'):
                valor_destino = valor
            else:
                print('Parámetro de Destino incorrecto')
        else:
            print('Parámetro de Origen incorrecto')
        return valor_destino

    def __factorial(self, numero):
        if(type(numero) != int):
            return 'El numero debe ser un entero'
        if(numero < 0):
            return 'El numero debe ser pisitivo'
        if (numero > 1):
            numero = numero * self.__factorial(numero - 1)
        return numero


"""
class multifuncion:
    def __init__(self, lista):
        self.lista = lista
    def primo(self):
        for i in self.lista:
            if self.__primo(i):
                print('El elemento', i, 'SI es un numero primo')
            else:
                print('El elemento', i, 'NO es un numero primo')
    
    def cuentalistas(self,trueofalse):
        if trueofalse== True:
            nuevodiccrepes=dict(zip(self.lista,map(lambda x: self.lista.count(x),self.lista)))
            return (f"el que mas se repite es el {max(nuevodiccrepes, key=nuevodiccrepes.get),nuevodiccrepes[max(nuevodiccrepes, key=nuevodiccrepes.get)]} veces") 
        else:
            nuevodiccrepes=dict(zip(self.lista,map(lambda x: self.lista.count(x),self.lista)))
            return (f" el que menos se repite es {min(nuevodiccrepes, key=nuevodiccrepes.get),nuevodiccrepes[min(nuevodiccrepes, key=nuevodiccrepes.get)]} veces")
    
    def conversion_grados(self, origen, destino):
        for i in self.lista:
            print(i, 'grados', origen, 'son', self.__conversion_grados(i, origen, destino),'grados',destino)

    def factorial(self):
        for n in self.lista:
            print(f"el factorial de {n} es {self.__factorial(n)}")
    def __init__(self) -> None:
        pass
    
    def __primo(self,numero):
        x =1
        c=0
        while x <= numero:
            if numero % x ==0:
             c+=1
            x+=1
        if c==2:
            return True
        else:
            return False
    
    def __cuentalistas(self,lista,trueofalse):
        if trueofalse== True:
            nuevodiccrepes=dict(zip(self.lista,map(lambda x: self.lista.count(x),self.lista)))
            return (f"el que mas se repite es el {max(nuevodiccrepes, key=nuevodiccrepes.get),nuevodiccrepes[max(nuevodiccrepes, key=nuevodiccrepes.get)]} veces") 
        else:
            nuevodiccrepes=dict(zip(self.lista,map(lambda x: self.lista.count(x),self.lista)))
            return (f" el que menos se repite es {min(nuevodiccrepes, key=nuevodiccrepes.get),nuevodiccrepes[min(nuevodiccrepes, key=nuevodiccrepes.get)]} veces")
    
    def __conversion_grados(self,valor, origen, destino):
        if (origen == 'celsius'):
            if (destino == 'celsius'):
                valor_destino = valor
            elif (destino == 'farenheit'):
                valor_destino = (valor * 9 / 5) + 32
            elif (destino == 'kelvin'):
                valor_destino = valor + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif (origen == 'farenheit'):
            if (destino == 'celsius'):
                valor_destino = (valor - 32) * 5 / 9
            elif (destino == 'farenheit'):
                valor_destino = valor
            elif (destino == 'kelvin'):
                valor_destino = ((valor - 32) * 5 / 9) + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif (origen == 'kelvin'):
            if (destino == 'celsius'):
                valor_destino = valor - 273.15
            elif (destino == 'farenheit'):
                valor_destino = ((valor - 273.15) * 9 / 5) + 32
            elif (destino == 'kelvin'):
                valor_destino = valor
            else:
                print('Parámetro de Destino incorrecto')
        else:
            print('Parámetro de Origen incorrecto')
        return valor_destino
        
    def __factorial(self,numero):
        if(type(numero) != int):
            return 'El numero debe ser un entero'
        if(numero < 0):
            return 'El numero debe ser positivo'
        if (numero > 1):
            numero = numero *self.factorial(numero - 1)
        return numero

m = multifuncion ([1,2,3,4,4,4])

"""

#8) Crear un archivo .py aparte y ubicar allí la clase generada en el punto anterior. Luego realizar la importación del módulo y probar alguna de sus funciones
from herramientas import *

h2 = Herramientas([1,1,2,3,5,6,8,8])
h2.conversion_grados('celsius','farenheit')