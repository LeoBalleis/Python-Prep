#1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla
lista = ['Buenos Aires','Asunción','Montevideo','Santiago','Lima','Caracas']
print(lista)
#2) Imprimir por pantalla el segundo elemento de la lista
print(lista[1])
#3) Imprimir por pantalla del segundo al cuarto elemento
print (lista[1:4])
#4) Visualizar el tipo de dato de la lista
print(type(lista))
#5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento
print(lista[2:])
#6) Visualizar los primeros 4 elementos de la lista
print(lista[:3])
#7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?
lista.append('Ciudad de Mejico')
lista.append('Ciudad de Mejico')
#8) Agregar otra ciudad, pero en la cuarta posición
lista.insert(3,"Caracas")
#9) Concatenar otra lista a la ya creada
lista2=[1,2,3,4,5,6,7,8]
lista+=lista2
lista.extend(['Madrid','Roma','Bruselas'])
print(lista)
#10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?
print(lista.index("Ciudad de Mejico"))# muestra el indice de la primer variable que encuentra 
#11) ¿Qué pasa si se busca un elemento que no existe?
#print(lista.index('París'))
#12) Eliminar un elemento de la lista
lista.remove('Buenos Aires')
#13) ¿Qué pasa si el elemento a eliminar no existe?
#lista.remove('Buenos Aires')
#14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo
ultimo = lista.pop()
print(ultimo)
#15) Mostrar la lista multiplicada por 4
print(lista*4)
#16) Crear una tupla que contenga los números enteros del 1 al 20
tupla= tuple(range(1,21))
print(tupla)
#17) Imprimir desde el índice 10 al 15 de la tupla
print(tupla[10:16])
#18) Evaluar si los números 20 y 30 están dentro de la tupla
print(20 in tupla)
print(30 in tupla)
#19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.

elemento = 'París'
if (not(elemento in lista)):
    lista.append(elemento)
    print('Se insertó el elemento', elemento)
else:
    print('El elemento', elemento, 'ya existía')



"""
elemento = 'París'
if elemento in lista:
    print('El elemento',elemento, 'ya existía')   
else:
    lista.append(elemento)
    print('Se insertó el elemento', elemento)
print(lista)
"""

#20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista
print(tupla.count(1))
print(lista.count('Montevideo'))
#21) Convertir la tupla en una lista
listupla=list(tupla)
print(listupla)
#22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables
primero, segundo, tercero = tupla[0], tupla[1], tupla[2]
print(primero,segundo,tercero)

#23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".
Diccionario={'ciudad':lista ,"Pais":['Brasil','Paraguay','Ecuador','Uruguay','Chile'],  "Continente":['america','america','america','america','america'] }
print(Diccionario)
#24) Imprimir las claves del diccionario
print(Diccionario.keys())
#25) Imprimir las ciudades a través de su clave
print(Diccionario["ciudad"])
