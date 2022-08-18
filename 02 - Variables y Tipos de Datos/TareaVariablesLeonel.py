#1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
from dataclasses import replace


numero1=1
#2) Imprimir el tipo de dato de la constante 8.5
print(type(8.5))
#3) Imprimir el tipo de dato de la variable creada en el punto 1
print(type(numero1))
#4) Crear una variable que contenga tu nombre
minombre="leonel"
#5) Crear una variable que contenga un número complejo
numerocomplejo=2+2j
#6) Mostrar el tipo de dato de la variable crada en el punto 5
print(type(numerocomplejo))
#7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
pi=3.141592
print(round(pi,4))
#8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
valortrue1=True
valortrue2="True"#No se tratan de lo mismo valortrue1 es un booleano y valortrue2 un string
#9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9
print(f'la variable 1 es {type(valortrue1)} y la variable 2 es {type(valortrue2)}')
#10) Asignar a una variable, la suma de un número entero y otro decimal
suma1= 2 + 2.3
print(suma1)
#11) Realizar una operación de suma de números complejos
sumacompleja= 2j + 2j
print(sumacompleja)
#12) Realizar una operación de suma de un número real y otro complejo
real=10
complejo=10j
sumarealcompleja=real+complejo
print (sumarealcompleja)
#13) Realizar una operación de multiplicación
multiplicación=2*10
#14) Mostrar el resultado de elevar 2 a la octava potencia
elevado=2**8
print(elevado)
#15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
cociente=27/4
print(cociente)
#16) De la división anterior solamente mostrar la parte entera
print(27 // 4)
#17) De la división de 27 entre 4 mostrar solamente el resto
print(27%4)
#18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
print((27 // 4) * 4 + (27%4))
#19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
concatenacion="hola"+"buenas"
print(concatenacion)
#20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
print(2 == '2')# estamos usando un operador condicional nos devuelve true o false
#21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
print(2 == int('2'))
#22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
a = '3,8'# estaban usando , en vez de . puede depender del sisteme operativo 
a=a.replace(',','.')
print(float(a))
#23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido
valor3=3
valor3-=1
print(valor3)
#24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
1<<2 # lo que hace  es agregar 2 ceros en foramto binario a la derecha  es util lo que pasa ahi es 1x2^2
    #1<<4 1x2^4
#25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
suma2=2 + int("2")# no se puede debidoa que los str no se pueden sumar con los int 
print(suma2)
suma3="2" + "2" # en este caso es una concatenacion 
print(suma3)
#26) Realizar una operación válida entre valores de tipo entero y string
var1 = 'este texto se repite '
var2 = 3
print(var1 * var2 + str(var2) + ' veces')
 