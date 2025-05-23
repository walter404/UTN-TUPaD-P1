"""1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
función para calcular y mostrar en pantalla el factorial de todos los números enteros 
entre 1 y el número que indique el usuario"""

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)

numero = int(input("Ingrese un numero: "))

for i in range(1, numero + 1):
    print(factorial(i))

"""2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
especifique."""

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
    
numero = int(input("Ingresar un numero: "))

for i in range(numero + 1):
    print(fibonacci(i))

"""3) Crea una función recursiva que calcule la potencia de un número base elevado a un 
exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un 
algoritmo general. """

def potencia(b, e):
    if e == 0:
        return 1
    else:
        return b * potencia(b, e - 1)

b = float(input("Ingrese un numero base: "))
e = int(input("Ingrese un exponente entero, no negativo: "))

resultado = potencia(b, e)

print(f"{b} elevado a la {e} es: {resultado}")

"""4) Crear una función recursiva en Python que reciba un número entero positivo en base 
decimal y devuelva su representación en binario como una cadena de texto. 
Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y 
unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este 
procedimiento: 
1. Dividir el número por 2. 
2. Guardar el resto (0 o 1). 
3. Repetir el proceso con el cociente hasta que llegue a 0. 
4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario. """

def binario(n): 
    if n == 0:#caso base, ahi de detiene la recursion
        return ""
    else:
        return binario(n // 2) + str(n % 2)# la funcion divide el numero por 2 y concatena el resto (n % 2) como una cadena
    
numero = int(input("Ingresar un numero entero positivo: "))

conversion = binario(numero)

print(f"El numero {numero} en binario es: {conversion}")

"""5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no 
lo es. 
    Requisitos: 
La solución debe ser recursiva. 
No se debe usar [::-1] ni la función reversed(). """

def es_palidromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    
    return es_palidromo(palabra[1:-1])


texto = input("Ingrese una palabra, sin tilde ni espacio: ").lower()

if es_palidromo(texto):
    print(f"{texto} es un polidromo")
else:
    print(f"{texto} no es un polidromo")

"""6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
número entero positivo y devuelva la suma de todos sus dígitos. 
    Restricciones: 
No se puede convertir el número a string. 
Usá operaciones matemáticas (%, //) y recursión. """

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)# n % 10 obtiene el ultimo digito del numero n//10 elimina el ultimo digito (divide entre 10 sin decimal)

numero = int(input("Ingres un numero: "))

resultado = suma_digitos(numero)

print(f"La suma de {numero} es: {resultado} ")

"""7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
último nivel con un solo bloque. 

Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
nivel más bajo y devuelva el total de bloques que necesita para construir toda la 
pirámide."""

def contar_bloques(n):
    if n == 1:
        return 1
    else: 
        return n + contar_bloques(n-1)

primer_nivel = int(input("Ingrese el numero de bloques del nivel bajo: "))

total = contar_bloques(primer_nivel)

print(f"El total de bloques es: {total}")


"""8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
aparece ese dígito dentro del número."""

def contar_digito(numero, digito):
    if numero < 10:
        if numero == digito:
            return 1
        else:
            return 0
    else:
        ultimo_numero = numero % 10 #obtenemos el ultimo digito del numero
        resto = numero // 10 #elimina el ultimo digito del numero

        if ultimo_numero == digito:
            return 1 + contar_digito(resto, digito)
        else:
            return 0 + contar_digito(resto, digito)

    
num = int(input("Ingrese un numero: "))
dig = int(input("Ingrese el digito a contar 0-9: "))

cantidad = contar_digito(num, dig)

print(f"El digito {dig} aparece {cantidad} veces,  en el numero {num}")