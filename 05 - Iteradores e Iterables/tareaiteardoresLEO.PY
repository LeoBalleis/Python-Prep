
#1) A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1

from operator import index

LISTANEG=[]
n=-15
while len(LISTANEG)<=14:
    LISTANEG.append (n)
    n+=1
print(LISTANEG)
print("-----------------------------------------------------------------------------------------------")
#2) ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?
for i in LISTANEG:
    while i%2==0:
        print (i)
        break
print("-----------------------------------------------------------------------------------------------")
#3) Resolver el punto anterior sin utilizar un ciclo while
for i in LISTANEG:
    if i%2==0:
        print(i)
print("-----------------------------------------------------------------------------------------------")

#4) Utilizar el iterable para recorrer sólo los primeros 3 elementos
lista3primeros=[]
n=1

for i in LISTANEG[:3]:
    print(i)
print("-----------------------------------------------------------------------------------------------")
#5) Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que corresponde el elemento
for i , x in enumerate(LISTANEG):
    print(f"numero de la lista¨{x} numero en orden {i} ")
print("-----------------------------------------------------------------------------------------------")
#6) Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: lista = [1,2,5,7,8,10,13,14,15,17,20]
lista20 = [1,2,5,7,8,10,13,14,15,17,20]
n = 1
while(n <= 20):
    if (not(n in lista20)):
        lista20.insert((n-1), n)
    n += 1
print(lista20)
print("-----------------------------------------------------------------------------------------------")
#7) La sucesión de Fibonacci es un listado de números que sigue la fórmula: <br>
#n<sub>0</sub> = 0<br>
#n<sub>1</sub> = 1<br>
#n<sub>i</sub> = n<sub>i-1</sub> + n<sub>i-2</sub><br>
#Crear una lista con los primeros treinta números de la sucesión.<br>
fibo = [0,1]
n = 2
while(n < 30):
    fibo.append(fibo[n-1]+fibo[n-2])
    n += 1
print(fibo)
print("-----------------------------------------------------------------------------------------------")

#8) Realizar la suma de todos elementos de la lista del punto anterior
print(sum(fibo))
print("-----------------------------------------------------------------------------------------------")
#9) La proporción aurea se expresa con una proporción matemática que nace el número irracional Phi= 1,618… que los griegos llamaron número áureo. El cuál se puede aproximar con la sucesión de Fibonacci. Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos números contiguos:<br>
#Donde i es la cantidad total de elementos<br>
#n<sub>i-1</sub> / n<sub>i</sub><br>
#n<sub>i-2</sub> / n<sub>i-1</sub><br>
#n<sub>i-3</sub> / n<sub>i-2</sub><br>
#n<sub>i-4</sub> / n<sub>i-3</sub><br>
#n<sub>i-5</sub> / n<sub>i-4</sub><br>
primeros = 15
n = primeros - 5
while(n < primeros):
    print(fibo[n]/fibo[n-1])
    n += 1
print("-----------------------------------------------------------------------------------------------")

#10) A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"<br>
cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'
for i, x in enumerate(cadena):
    if x == 'n':
        print(i)
print("-----------------------------------------------------------------------------------------------")

#11) Crear un diccionario e imprimir sus claves utilizando un iterador
diccionario={"numero1":1,"numero2":2,"numero3":3,"numero4":4}
for i in diccionario:
    print (i)
print("-----------------------------------------------------------------------------------------------")

#12) Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador 
cadena=list(cadena)
for i in cadena:
    print (i)
print(cadena)
print(type(cadena))
print("-----------------------------------------------------------------------------------------------")

#13) Crear dos listas y unirlas en una tupla utilizando la función zip
lista1=["hola","buen","dia"]
lista2=[1,2,3]
tuplamezclada=zip(lista1,lista2)
print(type(tuplamezclada))
tuplamezclada=list(tuplamezclada)
print(tuplamezclada)
print("-----------------------------------------------------------------------------------------------")

#14) A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7<br>
lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]
for i in lis:
    if i%7==0:
        print (i)
print("-----------------------------------------------------------------------------------------------")
      
#15) A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, teniendo en cuenta que un elemento de la lista podría ser otra lista:<br>
lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
cantidad = 0
for elemento in lis:
    if (type(elemento) == list):
        cantidad += len(elemento)
    else:
        cantidad += 1

print('La cantidad total de elementos es', cantidad)
print("-----------------------------------------------------------------------------------------------")

#16) Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es
for indice, elemento in enumerate(lis):
    if (type(elemento) != list):
        lis[indice]=[elemento]
print(lis)