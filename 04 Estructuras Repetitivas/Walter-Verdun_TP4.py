"""1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea."""

for i in range(101):
    print(i)

"""2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
dígitos que contiene."""

num = int(input("Introduce un número entero: "))
cont = 0
while num > 0:
    num //= 10  # Dividir el número por 10 elimina el último dígito
    cont += 1
print("La cantidad de dígitos es:", cont)

"""3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
dados por el usuario, excluyendo esos dos valores. """

num1 = int(input("Introduce el primer valor: "))
num2 = int(input("Introduce el segundo valor: "))

if num1 > num2:
    num1, num2 = num2, num1

suma = sum(range(num1 + 1, num2)) 
print("La suma de los números comprendidos entre", num1, "y", num2, "es:", suma)

"""4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
un 0."""

num = int(input("Introduce un número entero (0 para salir): "))
suma = 0
while num != 0:
    suma += num
    num = int(input("Introduce un número entero (0 para salir): "))
    

print("La suma total es:", suma)

"""5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
programa debe mostrar cuántos intentos fueron necesarios para acertar el número."""

import random
num_aleatorio = random.randint(0, 9) # Genera un número aleatorio entre 0 y 9
intentos = 0
adivinado = False   # Variable para controlar si se adivinó el número

while not adivinado:
    intento = int(input("Adivina el número entre 0 y 9: "))
    intentos += 1
    if intento == num_aleatorio:
        adivinado = True
    else:
        print("Intenta de nuevo.")
print("¡Felicidades! Adivinaste el número", num_aleatorio, "en", intentos, "intentos.")

"""6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
entre 0 y 100, en orden decreciente."""

for i in range(100, -1, -1): # Decrementa de 100 a 0
    if i % 2 == 0:  # Verifica si el número es par
        print(i)

"""7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
número entero positivo indicado por el usuario. """

numero = int(input("Introduce un número entero positivo: "))

if numero > 0:
    suma = 0
    for i in range(1, numero + 1): #Suma de 1 hasta el número ingresado
        suma += i
    print("La suma de los números de 1 a", numero, "es:", suma)
else:
    print("Debes introducir un número entero positivo.")

"""8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
menor, pero debe estar preparado para procesar 100 números con un solo cambio)."""

num_pares = 0
num_impares = 0
num_positivos = 0
num_negativos = 0

for i in range(100):
    num = int(input("Introduce un número entero: "))
    if num % 2 == 0:
        num_pares += 1
    else:
        num_impares += 1
    if num > 0:
        num_positivos += 1
    elif num < 0:
        num_negativos += 1

"""9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
poder procesar 100 números cambiando solo un valor)."""

suma = 0
for i in range(100):
    num = int(input("Introduce un número entero: "))
    suma += num
media = suma / 100 # Calcula la media dividiendo la suma total entre 100
print("La media de los números ingresados es:", media)

"""10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745."""

num = int(input("Introduce un número entero: "))
num_invertido = 0
while num > 0:
    digito = num % 10 # Obtiene el último dígito del número
    num_invertido = num_invertido * 10 + digito # Agrega el dígito al final del número invertido
    num //= 10  # Elimina el último dígito del número original
print("El número invertido es:", num_invertido)
