"""1) Dado el diccionario precios_frutas """

precios_frutas = {'Banana': 1200, 'Anana': 2500, 'Melon': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

"""2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: """

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melon'] = 2800

print(precios_frutas)

"""3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
precios. """

nombre_frutas = precios_frutas.keys()
print(nombre_frutas)

"""4) Escribí un programa que permita almacenar y consultar números telefónicos. 
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
• Luego, pedí un nombre y mostrale el número asociado, si existe. """

contactos = {"Pablo": "324221", "Ana": "45215"}

for i in range(3):
    nombre = input(f"Ingresa nombre de contacto {i+1}: ")
    numero = input(f"Ingresa numero del contacto {nombre}: ")
    contactos[nombre] = numero

buscar_contacto = input(f"Ingrese el nombre del contacto que dese buscar: ")

if buscar_contacto in contactos:
    print(f"El numero de {buscar_contacto} es {contactos[buscar_contacto]}")
else:
    print(f"No se encuentra el contacto con el nombre '{buscar_contacto}'")

"""5) Solicita al usuario una frase e imprime: 
• Las palabras únicas (usando un set). 
• Un diccionario con la cantidad de veces que aparece cada palabra. """

usuario_frase = input("Ingrese una frase: ")

#Convertimo la frase en una lista de palablas
frases = usuario_frase.split()

#Creamos el set 
palabras_unicas = set(frases)
print("Palabras unicas: ", palabras_unicas)

#Creamos diccionario para la cantidad de veces que aparece cada palabra
recuento = {}

for frase in  frases:
    if frase in recuento:
        recuento[frase] += 1
    else:
        recuento[frase] = 1

print(recuento)

"""6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
Luego, mostrá el promedio de cada alumno. """

nombre_alumnos = {}

for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    nota1 = int(input("Nota 1: "))
    nota2 = int(input("Nota 2: "))
    nota3 = int(input("Nota 3: "))
    nombre_alumnos[nombre] = (nota1, nota2, nota3)

print("\nPromedios: ")
for nombre, notas in nombre_alumnos.items():
    promedio = (notas[0] + notas[1] + notas[2]) / 3
    print(f"{nombre_alumnos}: {promedio:.2f}")

"""7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
y Parcial 2: 
• Mostrá los que aprobaron ambos parciales. 
• Mostrá los que aprobaron solo uno de los dos. 
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). """

parcial1 = {"Pablo", "Juana", "Martin", "Pedro", "Lucas"}
parcial2 = {"Juana", "Pablo", "Lautaro", "Esteban", "Patricia"}

#Se utiliza & para interseccion 
ambos_paciales = parcial1 & parcial2
print("Aprobaron ambos parciales: ", ambos_paciales)

#Se utiliza ^ para diferencia simetrica
solo_uno = parcial1 ^ parcial2
print("Aprobaron solo uno de los dos: ", solo_uno)

#Se utiliza | para unio 
al_menos_un_parcial = parcial1 | parcial2
print("Aprobaron al menos un parcial: ", al_menos_un_parcial)

"""8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
Permití al usuario: 
• Consultar el stock de un producto ingresado. 
• Agregar unidades al stock si el producto ya existe. 
• Agregar un nuevo producto si no existe. """

stock = {
    "Lapiz": 500,
    "Regla": 1500,
    "Goma": 600
}

# Ingrea el producto a modificar sino a consultar
producto = input("Ingresa el nombre del producto: ")

if producto in stock:
    print(f"Stock actual de {producto}: {stock[producto]} unidades")
    #Preguntamos si quiere agregar unidades
    agregar = input("¿Desea agregar unidades? (si/no): ").lower()
    if agregar == "si":
        unidades = int(input("¿Cuantas unidades quieres agregar?: "))
        stock[producto] += unidades
        print(f"Nuevo stock de {producto}: {stock[producto]} unidades")
else:
    print(f"{producto} no esta en el sistema")
    agregar_nuevo = input("¿Queres agregarlo como nuevo producto? (si/no): ").lower()
    if agregar_nuevo == "si":
        unidades = int(input(f"Ingresa el stock inicial para {producto}: "))
        stock[producto] = unidades
        print(f"{producto} agregado con {unidades} unidades.")

"""9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. """

agenda = {}

agenda[("Lunes", "09:00")] = "Organizar tareas"
agenda[("Martes", "14:30")] = "Mirar clase Grabada"
agenda[("Miercoles", "11:00")] = "Realizar Trabajo Practico"

#Mostrar agenda con todos los datos
print("Agenda semanal: ")
for (dia, hora), evento in agenda.items():
    print(f"{dia} a las {hora}: {evento}")

"""10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
diccionario donde: 
• Las capitales sean las claves. 
• Los países sean los valores. """

original = {
    "Argentina": "Buenos Aires",
    "Italia": "Roma",
    "Israel": "Jerusalen",
    "Brasil": "Brasilia"
}

#Se invierte el diccionario
invertido = {}

for pais, capital in original.items():
    invertido[capital] = pais

#Mostrar resultado de ambos 
print("Diccionario original: ", original)
print("Diccionario invertido: ", invertido)