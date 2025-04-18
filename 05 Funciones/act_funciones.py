#1.Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

#definicion de la funcion.
def imprimir_hola_mundo():
    print ("hola mundo")

#prpgrama principal

imprimir_hola_mundo()

#2Crear una función llamada saludar_usuario(nombre) que recibacomo parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

#definicion de la funcion.

def saludar_usuario(nombre):
    saludo = f"Hola {nombre}!"
    return saludo
    
#programa principal

nombre_usuario = input("Ingrese su nombre: ")
mensaje_saludo = saludar_usuario(nombre_usuario)
print(mensaje_saludo) 

#3.Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados

#definicion de la funcion.

def informacion_personal(nombre,apellido,edad,residencia):
    informacion = f"soy {nombre} {apellido} tengo {edad} años y vivo en {residencia}"
    return informacion

#programa principal

nombre = input("ingrese su nombre: ")
apellido = input("ingrese su apellido: ")
edad = input("ingrese su edad: ")
residencia = input("inrgese su residencia: ")

info_personal = informacion_personal(nombre,apellido,edad,residencia)
print(info_personal)

#4.Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
#calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
#Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

#definicion de la funcion.

import math
pi = math.pi
def calcular_area_circulo(radio):
     area = pi * radio ** 2
     return area

def calcular_perimetro_circulo(radio):
     perimetro = pi * radio * 2
     return perimetro

#programa principal

radio = float(input("ingrese el radio: "))
area = calcular_area_circulo(radio)
print(f"el area es: {area}.")


perimetro = calcular_perimetro_circulo(radio)
print(f"el perimetro es de: {perimetro}")

#5.Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

#definicion de la funcion.

def segundos_a_horas(segundos):
    """Convierte una cantidad de segundos a horas."""
    horas = segundos / 3600
    return horas

# Programa principal
try:
    segundos_totales_str = input("Ingrese la cantidad de segundos: ")
    segundos_totales = int(segundos_totales_str)
    horas_resultantes = segundos_a_horas(segundos_totales)
    print(f"{segundos_totales} segundos equivalen a {horas_resultantes} horas.")
except ValueError:
    print("¡Entrada inválida! Por favor, ingrese un número entero para los segundos.")

print("Fin del programa.")

#6.Crear una función llamada tabla_multiplicar(numero) que reciba unnúmero como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función.

#definicion de la funcion.

def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1,11):
        resultado = i * numero
        print(resultado)

# Programa principal

num = int(input("ingrese un numero"))
tabla_multiplicar(num)

#7.Crear una función llamada operaciones_basicas(a, b) que recibados números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
#Mostrar los resultados de forma clara.

#definicion de la funcion.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b == 0:
        division = "No se puede dividir por cero"
    else:
        division = a / b
    resultados = (suma, resta, multiplicacion, division)
    return resultados

# Programa principal
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
resultados_tupla = operaciones_basicas(num1, num2)

suma_res, resta_res, multiplicacion_res, division_res = resultados_tupla

print(f"Suma: {suma_res}")
print(f"Resta: {resta_res}")
print(f"Multiplicación: {multiplicacion_res}")
print(f"División: {division_res}")

#8.Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). 
# Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

#definicion de la funcion.

def calcular_imc(peso, altura):
    print(f"tu indice de masa corporal es: {imc_calculado:.2f}")
    imc = peso / (altura **2)
    return imc

# Programa principal

peso = float(input("ingrese su peso: "))
altura = float(input("ingrese su altura"))


imc_calculado = calcular_imc(peso,altura)

#9.Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. 
#Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

#definicion de la funcion.

def celsius_a_fahrenheit(celsius):
    pasaje = (celsius * 9/5) + 32
    return pasaje

# Programa principal

temp_celius = float(input("ingrese la temperatura en celsuis: "))
print("la temperatura en fahrengeit", celsius_a_fahrenheit(temp_celius))

#10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta función.

#definicion de la funcion.

def calcular_promedio(a,b,c):
    media = (a + b + c) / 3
    return media

# Programa principal

num = int(input("ingrese el primer numero: "))
num1 = int(input("ingrese el segundo numero: "))
num2 = int(input("ingrese el tercer numero: "))

promedio_calculado = calcular_promedio(num, num2,num2)
print("El promedio es:", promedio_calculado)


