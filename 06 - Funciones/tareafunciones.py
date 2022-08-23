#1) Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es
from re import X


def main(numero):
    x=1
    c=0
    while x <= numero:
        if numero % x ==0:
            c+=1
        x+=1
    if c==2:
        return True
    else:
        return False
print(main(1))        
print("------------------------------------------------------------------------------------")
#2) Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de números y devuelva sólo aquellos que son primos en otra lista
listarandom=[1,2,3,4,5,6,7,8,9,10]
def devolverprimos(lista):
    listaprimos=[]
    for i in lista:
        if main(i):
            listaprimos.append(i)
    return listaprimos

print(devolverprimos(listarandom))
print("------------------------------------------------------------------------------------")
   
#3) Crear una función que al recibir una lista de números, devuelva el que más se repite y cuántas veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera
listaderepe=[1,2,2,2,3,4,5,6,6,7]
def cuentalistas(lista):   
    nuevodiccrepes=dict(zip(lista,map(lambda x: lista.count(x),lista)))
    return max(nuevodiccrepes, key=nuevodiccrepes.get) 
    
print(f"el que mas se repite es el {cuentalistas(listaderepe)}" )

"""
def valor_modal(lista):
    lista_unicos = []
    lista_repeticiones = []
    if len(lista) == 0:
        return None
    for elemento in lista:
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
"""

print("------------------------------------------------------------------------------------")
#4) A la función del punto 3, agregar un parámetro más, que permita elegir si se requiere el menor o el mayor de los mas repetidos.
listaderepe=[1,2,2,2,3,4,5,6,6,7]
def cuentalistas(lista,trueofalse):
    if trueofalse== True:
        nuevodiccrepes=dict(zip(lista,map(lambda x: lista.count(x),lista)))
        return max(nuevodiccrepes, key=nuevodiccrepes.get) 
    else:
        nuevodiccrepes=dict(zip(lista,map(lambda x: lista.count(x),lista)))
        return min(nuevodiccrepes, key=nuevodiccrepes.get) 

print(f"el que menos se repite es el {cuentalistas(listaderepe,False)}" )
print(f"el que mas se repite es el {cuentalistas(listaderepe,True)}" )
print("------------------------------------------------------------------------------------")
#5) Crear una función que convierta entre grados Celsius, Farenheit y Kelvin<br>
#Fórmula 1	: (°C × 9/5) + 32 = °F<br>
#Fórmula 2	: °C + 273.15 = °K<br>
#Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino
def conversion_grados(valor, origen, destino):
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

print(conversion_grados(60,'celsius','farenheit'))
print("------------------------------------------------------------------------------------")

#6) Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:

metricas = ['celsius','kelvin','farenheit']
for i in range(0,3):
    for j in range(0,3):
        print('1 grado', metricas[i], 'a', metricas[j],':', conversion_grados(1, metricas[i], metricas[j]))

print("------------------------------------------------------------------------------------")


#7) Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o negativo

def factorial(numero):
    if(type(numero) != int):
        return 'El numero debe ser un entero'
    if(numero < 0):
        return 'El numero debe ser positivo'
    if (numero > 1):
        numero = numero * factorial(numero - 1)
    return numero
print(factorial(5))
print(factorial(5.4))
print(factorial(-5))



