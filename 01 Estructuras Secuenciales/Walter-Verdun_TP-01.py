#Actividad 1
"""Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”."""

print("Hola Mundo!")

#Activida 2
"""Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir 
por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para 
realizar la impresión por pantalla."""

nombre= input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

#actividad 3
"""Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 
años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar 
la impresión por pantalla."""

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar_recidencia = input("Ingrese su recidencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} anios y vivo en {lugar_recidencia}")

#actividad 4
"""Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
su perímetro."""

import math

#Se solicita el radio
radio = float(input("Ingrese el radio del circulo: "))

#Se calcula el area y perimetro
area = math.pi * radio**2
perimetro = 2 * math.pi * radio

#Se imprime los resultados
print(f"Area del circulo: {area:.2f}")
print(f"Perimetro del circulo: {perimetro:.2f}")

#actividad 5
"""Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
cuántas horas equivale."""

segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas:.2f} horas")

#actividad 6
"""Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
multiplicar de dicho número."""

numero = int(input("Ingrese un numero: "))

print(f"Tabla de multiplicar {numero}: ")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

#actividad 7
"""Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos."""

numero1 = int(input("Ingrese primer numero (distinto de 0): "))
numero2 = int(input("Ingrese segundo numero (distinto de 0): "))

#Se verifica si los numeros ingresados son distintos a 0
if numero1 == 0 or numero2 == 0:
    print("Error los numeros ingresados deben ser distintos a 0")
else:
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2

    print(f"Suma: {numero1} + {numero2} = {suma}")
    print(f"Resta: {numero1} + {numero2} = {resta}")
    print(f"Multiplicacion: {numero1} + {numero2} = {multiplicacion}")
    print(f"Division: {numero1} + {numero2} = {division:.2f}")

#actividad 8
"""Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
de masa corporal."""

altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))

imc = peso / (altura ** 2)
print(f"Su indice de Masa Corporal es: {imc:.2f}")

#actividad 9
"""Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
pantalla su equivalente en grados Fahrenheit."""

temperatura_celsius = float(input("Ingrese una temperatura en grados Celsius: "))

fahrenheit = (temperatura_celsius * 9/5) + 32
print(f"{temperatura_celsius}°C esto equivale a {fahrenheit:.2f}°F")

#activida 10
"""Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de 
dichos números."""

numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))
numero3 = float(input("Ingrese el tercer numero: "))

promedio = (numero1 + numero2 + numero3) / 3
print(f"El promedio de {numero1}, {numero2}, {numero3} es: {promedio:.2f}")