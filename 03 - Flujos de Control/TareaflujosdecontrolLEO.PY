#1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero
numero1=1
if numero1>0:
    print(f'{numero1} es mayor a 0')
elif numero1<0:
    print(f'{numero1} es menor a 0 ')
else:
    print('el numero es 0 ')
print('#############################################################################################################')
#2) Crear dos variables y un condicional que informe si son del mismo tipo de dato
variable=1
variable2="hola"
if type(variable)==type(variable2):
    print (f'son el mismo tipo de dato {type(variable)} ')
else:
    print(f'no son el mismo tipo de dato variable es:{type(variable)} y variable2 es: {type(variable2)} ')
print('#############################################################################################################')   
#3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar
for numeroparoimpar in range(1,21):
    if numeroparoimpar%2==0:
        print(f"el numero {numeroparoimpar} es par.")
    else:
        print(f"el numero {numeroparoimpar} es impar  ") 
print('#############################################################################################################')
#4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3
for numeroelevado in range (0,6):
    print(f"{numeroelevado}elevado a la 3 es {numeroelevado**3}")
print('#############################################################################################################')
#5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos
variablenumeroentero= 10
ciclo=0
for i in range(0,variablenumeroentero): 
    ciclo+=1
    print(f"este es el ciclo numero {ciclo}")
print('#############################################################################################################')
#6) Utilizar un ciclo while para realizar el factorial de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0
#n = int(input("ingrese un numero entero mayor a 0: "))
n=10
if (type(n) == int):
    if (n > 0):
        factorial = n
        while (n >= 2):
            n -= 1
            factorial = factorial * n
        print('El factorial es', factorial)
    else:
        print('La variable no es mayor a cero')
else:
    print('La variable no es un entero')
print('#############################################################################################################')
#7) Crear un ciclo for dentro de un ciclo while
contador=0
while contador<=3:
    contador+=1
    for numerin in range(0,2):
        print ('esto es un bucle en un bucle')
print('#############################################################################################################')
#8) Crear un ciclo while dentro de un ciclo for
for wile in ('12'):
    print(f"bucle for numero {wile}")
    contador=0
    while contador<=1:
        print(f'esto es un bucle while dentro de un for ')
        contador+=1
print('#############################################################################################################')
#9) Imprimir los números primos existentes entre 0 y 30

for primo in range (0,31):
    x=1
    c=0
    while x <= primo:
        if primo % x ==0:
            c+=1
        x+=1
    if c==2:
        print(f'el numero {primo} es primo ')
    else:
        print(f'el numero {primo} no es primo ')

print('#############################################################################################################')
#10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin
'''
CODIGO EJERCICIO 9 RESUELTOS:
tope_rango=30
n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        if (n % div == 0):
            primo = False
    if (primo):
        print(n)
    else:
        primo = True
    n += 1
'''
#SI SE PUEDE MEJORAR 
n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        if (n % div == 0):
            primo = False
            break
    if (primo):
        print(n)
    else:
        primo = True
    n += 1

print('#############################################################################################################')
#11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?
ciclos_sin_break = 0
n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        ciclos_sin_break += 1
        if (n % div == 0):
            primo = False
    if (primo):
        print(n)
    else:
        primo = True
    n += 1
print('Cantidad de ciclos: ' + str(ciclos_sin_break))

ciclos_con_break = 0
n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        ciclos_con_break += 1
        if (n % div == 0):
            primo = False
            break
    if (primo):
        print(n)
    else:
        primo = True
    n += 1
print('Cantidad de ciclos: ' + str(ciclos_con_break))
print('Se optimizó a un ' + str(ciclos_con_break/ciclos_sin_break) + '% de ciclos aplicando break')

print('#############################################################################################################')
#12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?
tope_rango=100
ciclos_sin_break = 0
n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        ciclos_sin_break += 1
        if (n % div == 0):
            primo = False
    if (primo):
        print(n)
    else:
        primo = True
    n += 1
print('Cantidad de ciclos: ' + str(ciclos_sin_break))
print('#############################################################################################################')
#13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300
n = 99
while(n <= 300):
    n += 1
    if (n % 12 != 0):
        continue
    print(n, ' es divisible por 12')
print('#############################################################################################################')
#14) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente
n = 1
sigue = 1
primo = True
while (sigue == 1):
    for div in range(2, n):
        if (n % div == 0):
            primo = False
            break
    if (primo):
        print(n)
        print('¿Desea encontrar el siguiente número primo?')
        if (input() != '1'):
            print('Se finaliza el proceso')
            break
    else:
        primo = True
    n += 1
print('#############################################################################################################')
#15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6
n = 100
while(n<=300):
    if (n % 6 == 0):
        print('El número es: ', str(n))
        break
    n += 1

while(n>=100):
    if (n % 6 == 0):
        print('El número es: ', str(n))
        break
    n += 1