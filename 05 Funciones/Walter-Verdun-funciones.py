""" 1. Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal."""

#funcion llamada imprimir_hola_mundo
def inmprimir_hola_mundo():
    #imprimir el mensaje
    print("Hola Mundo!")
#llamar la funcion
inmprimir_hola_mundo()

"""2. Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
volver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario."""

#funcion llamada saludar_usuario
def saludar_usuario(nombre):
    #saludo personalizado
    return f"Hola {nombre}!"

#Solucitar al usuario el nombre
nombre_saludar = input("Ingrese su nombre: ")
#llamar la funcion
print(saludar_usuario(nombre_saludar))

"""3. Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe
dir los datos al usuario y llamar a esta función con los valores in
gresados."""

#funcion llamada informacion_personal
def informacion_personal(nombre, apellido, edad, residencia):
    #imprimir la informacion personal
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#Solicitar los datos al usuario
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")

#llamar la funcion
informacion_personal(nombre, apellido, edad, residencia)

""" 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
dio como parámetro y devuelva el área del círculo. calcular_peri
metro_circulo(radio) que reciba el radio como parámetro y devuel
va el perímetro del círculo. Solicitar el radio al usuario y llamar am
bas funciones para mostrar los resultados."""

#crear la funcion calcular_area_circulo
def calcular_area_circulo(radio):
    #calcular el area
    area = 3.14 * radio ** 2
    #devover el area
    return area

#Creamos la funcion calcular_perimetro_circulo
def calcular_perimetro_circulo(radio):
    #calculamos el perimetro 
    perimetro = 2 * 3.14 * radio
    #devolvemos el perimetro
    return perimetro

#solicitar el radio al usuario
usuario_radio = float(input("Ingrese el radio del circulo: "))
#llamar la funcion calcular_area_circulo
area = calcular_area_circulo(usuario_radio)
#llamar la funcion calcular_perimetro_circulo
perimetro = calcular_perimetro_circulo(usuario_radio)

#printar los resultados
print(f"El area del circulo es: {area}")
print(f"El perimetro del circulo es: {perimetro}")

"""5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mos
trar el resultado usando esta función."""

def segundos_a_horas(segundos):
    #convertir segundos en horas
    horas= segundos / 3600
    #devolver el resultado
    return horas

#Slocitamos al usuario los segundos
ingreso_segundos = int(input("Ingrese los segundos: "))

#Llmamos a la funcion
resultado = segundos_a_horas(ingreso_segundos)
#Mostramos el resultado
print(f"Los segundos ingresados son: {resultado} horas")


"""6. Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la fun
ción."""

def tabla_multiplicar(numero):
    #creamos un bucle for para imprimir la tabla de multiplicar
    for i in range(1, 11):
        #imprimimos la tabla
        print(f"{numero} x {i} = {numero * i}")

#solicitamos al usuario el numero
numero_usuario = int(input("Ingrese un numero: "))
#llamamos a la funcion
tabla_multiplicar(numero_usuario)

""" 7. Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resulta
do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
sultados de forma clara."""

def operacciones_basicas(a, b):
    #se realizan las operacionces
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    #creamos una condicion para evitar la division por cero
    if b != 0:
        division = a / b
        print("No se puede dividir por cero")
    else:
        division = "division por cero no es posible"
    #se devuelve el resultado
    return suma, resta, multiplicacion, division

#duevuelvo la tupla 
resultado = operacciones_basicas(10, 0)
#imprimo el resultado
print(f"La suma es: {resultado[0]}")
print(f"La resta es: {resultado[1]}")
print(f"La multiplicacion es: {resultado[2]}")
print(f"La division es: {resultado[3]}")

""" 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
ción para mostrar el resultado con dos decimales."""

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# Solicitar al usuario el peso y la altura
solicitud_peso = float(input("Ingrese su peso en kg: "))
solicitud_altura = float(input("Ingrese su altura en metros: "))

# Llamar a la función calcular_imc
resultado_imc = calcular_imc(solicitud_peso, solicitud_altura)
# Mostrar el resultado
print(f"Su IMC es: {resultado_imc:.2f}") #.2f es para mostrar 2 decimales

"""9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función."""

def celsius_a_fahrenheit(celsius):
    #convertir celsius a fahrenheit
    fahrenheit = (celsius * 9/5) + 32 #  9/5 es la conversion de celsius a fahrenheit + 32 es la temperatura de congelacion
    #devolver el resultado
    return fahrenheit

#solicitamos al usuario la temperatura en celsius
temperatura_celsius = float(input("Ingrese la temperatur en Celsius: "))

#llamamos a la funcion
resultado_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)
#mostramos el resultado
print(f"La temperatura en Fahrenheit es: {resultado_fahrenheit:.2f}") #.2f es para mostrar 2 decimales


"""10.Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función."""


def calcular_promedio(a, b, c):
    #calculamos el promedio
    promedio = (a + b + c) / 3 # promedio de 3 numeros
    #devolvemos el resultado
    return promedio

#solicitamos al usuario los 3 numeros
numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))
numero3 = float(input("Ingrese el tercer numero: "))

#llamamos a la funcion
resultado_promedio = calcular_promedio(numero1, numero2, numero3)
#mostramos el resultado
print(f"El promedio de los 3 numeros es: {resultado_promedio:.2f}") #.2f es para mostrar 2 decimales
