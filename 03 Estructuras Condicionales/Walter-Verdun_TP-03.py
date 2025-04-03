""" 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”."""

edad = int(input("Por favor ingrese su edad: "))

if edad > 18 :
    print("Es mayor de edad")


"""2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
mensaje “Desaprobado”."""

nota = float(input("Ingrese su nota: "))

if nota >= 6 :
    print("Aprobado")
else :
    print("Desaprobado")

"""3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
operador de módulo (%) en Python para evaluar si un número es par o impar."""

numeros_pares = int(input("Escriba un numero par: "))

if numeros_pares % 2 == 0:
    print("Ha ingresado un numero par")
else :
    print("Por favor, ingresar un numero par.")

"""4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
siguientes categorías pertenece: 
● Niño/a: menor de 12 años. 
● Adolescente: mayor o igual que 12 años y menor que 18 años. 
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
● Adulto/a: mayor o igual que 30 años."""

edad = int(input("Por favor ingrese su edad: "))

if edad < 12 :
    print("Eres Niño/a.")
elif 12 <= edad < 18 :
    print("Eres adolecente.")
elif   18<= edad < 30 :
    print("Eres Adulto/a joven")
else:
    print("Eres Adulto/a.")


"""5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
como una lista o un string."""

contraseña = input("Ingrese una contraseña: ")

if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else: 
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


"""6) escribir un programa que tome la lista 
numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla."""

import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print(f"Media: {media}")
print(f"Media: {mediana}")
print(f"Media: {moda}")

if media > mediana > moda:
    print("Sesgo positivos")
elif media < mediana < moda:
    print("Sesgo negativo")
else:
    print("No hay sesgo")

"""7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
pantalla."""

frase_palabra = input("Por favor ingrese una frace o palabra: ")

if frase_palabra and frase_palabra[-1].lower() in "aeiou":  # Metodo lower() hace que todas las letras en minuscula.
    frase_palabra += "!"
else:
    frase_palabra = frase_palabra

print(frase_palabra)

"""8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
dependiendo de la opción que desee: 
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro."""

nombre = input("Ingrese su nombre: ")
numero_opcion = input("Ingrese 1  mayúsculas, 2 minúsculas, 3 primera letra mayúscula: ")

if numero_opcion == "1":
    print(nombre.upper()) # el metodo upper() convierte a la cadena de texto en mayúsculas.
elif numero_opcion == "2":
    print(nombre.lower()) # el metodo lower() convierte a la cadena de texto en minúsculas.
elif numero_opcion == "3":
    print(nombre.title()) # el metodo title() convierte a la primera letra en mayúscula.
else:
    print("La opcion seelccionada es invalida. Debe ingresar 1, 2 o 3.")

"""9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
por pantalla."""

magnitud_terremoto = float(input("Ingrese la magnitu de un terremoto: "))

if magnitud_terremoto < 3:
    print("Muy leve (imperceptible).")
elif   3 <= magnitud_terremoto < 4:
    print("Leve (ligeramente perceptible).")
elif 4 <= magnitud_terremoto < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif 5 <= magnitud_terremoto < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif 6 <= magnitud_terremoto < 7:
    print("Muy fuerte (puede causar daños significativos).")
else : 
    print("Extrem (puede causar graves daños a gran escala).")

"""10)Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. 
El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano."""

hemisfero = input("Ingrese cuál hemisfero se ebcuentra (N/S): ").strip().upper()
mes = int(input("Ingrese el mes actual: "))
dia = int(input("Ingrese el dia del mes: "))

if hemisfero == "N":  # Hemisferio Norte
    if (mes  == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        print("Invierno")
    elif (mes  == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        print("Primavera")
    elif (mes  == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
        print("Verano")
    else:
        print("Otoño")
        
elif hemisfero == "S":  # Hemisferio Sur
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        print("Verano")
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        print("Otoño")
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
        print("Invierno")
    else:
        print("Primavera")

else:
    print("Hemisferio no válido. Ingrese 'N' o 'S'.")

