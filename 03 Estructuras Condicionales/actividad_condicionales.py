#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("ingrese su edad: "))
if edad >= 18:
    print("es mayor de edad.")


 #2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
#mensaje “Desaprobado”.

nota = int(input("ingrese nota: "))
if 6 <= nota:
    print("aprobado.")
else:
    print("desaprobado.")

 #3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
#operador de módulo (%) en Python para evaluar si un número es par o impar.

numero = int(input("ingrese un numero par: "))
if numero % 2 == 0:
    print("el numero ingresado es par.")
else:
    print("por favor, ingrese un numero par.")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
#siguientes categorías pertenece: 
#● Niño/a: menor de 12 años. 
#● Adolescente: mayor o igual que 12 años y menor que 18 años. 
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
#● Adulto/a: mayor o igual que 30 años.

edad = int(input("ingrese su edad: "))
if edad < 12:
    print("niño/a.")
elif edad >= 12 and edad < 18:
    print("adolecente.")
elif edad >= 18 and edad <30:
    print("adulto/a joven.")
else:
    print("adulto/a")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
#como una lista o un string

contraseña = input("ingrese una contraseña entre 8 y 14 carecteres: ")
contraseña_longitud = len(contraseña)
if contraseña_longitud >= 8 and contraseña_longitud <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


#6) El paquete statistics de python contiene funciones que permiten tomar una lista de números 
#y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el 
#siguiente: 
#from statistics import mode, median, mean 
#mi_lista = [1,2,5,5,3] 
#mean(mi_lista) 
#En la documentación oficial se puede encontrar más información sobre este paquete: 
#https://docs.python.org/es/3.8/library/statistics.html.  
#La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se 
#pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio: 
#● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la 
#mediana es mayor que la moda. 
#● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, 
#la mediana es menor que la moda. 
#● Sin sesgo: cuando la media, la mediana y la moda son iguales. 
#Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista 
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. 
#Definir la lista numeros_aleatorios de la siguiente forma: 
#import random 
#numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 
#Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de 
#forma aleatoria. 

import random
from statistics import mode, median, mean
# Generar la lista de números aleatorios
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# Calcular la moda, la mediana y la media
moda_numeros = mode(numeros_aleatorios)
mediana_numeros = median(numeros_aleatorios)
media_numeros = mean(numeros_aleatorios)
# Comparar los parámetros y determinar el sesgo
if media_numeros > mediana_numeros > moda_numeros:
    print("Sesgo positivo o a la derecha.")
elif media_numeros < mediana_numeros < moda_numeros:
    print("Sesgo negativo o a la izquierda.")
else:
    print("Sin sesgo.")



#7)Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
#pantalla.

frase = str(input("escribe una frase: "))
ultima_letra = frase[-1].lower()

if ultima_letra in "a,e,i,o,u":
    print(f"{frase}!")
else:
    print(f"{frase}")


#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
#dependiendo de la opción que desee: 
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre= str(input("ingrese su nombre"))
numero = int(input("ingrese un 1:todo mayucula, 2:todo minuscula o 3:primera letra mayuscular"))

if numero == 1:
    nombre = nombre.upper()
    print (nombre)
elif numero ==2:
    nombre = nombre.lower()
    print (nombre)
elif numero == 3:
    nombre = nombre.title()
    print(nombre)
else:
    print("numero ingresado incorrecto") 

 #9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
#por pantalla: 
#● Menor que 3: "Muy leve" (imperceptible). 
#● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
#● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
#generalmente no causa daños). 
# ● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
# débiles). 
# ● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud_terremoto = float(input("ingrese la magnitud del terrremoto"))

if magnitud_terremoto < 3:
    print("muy leve(imperceptible)")
elif magnitud_terremoto >= 3 and magnitud_terremoto < 4:
    print("leve (ligeramente perceptible)")
elif magnitud_terremoto >= 4 and magnitud_terremoto < 5:
    print("moderado(sentido por personas, pero generalmente no causa daños)")
elif magnitud_terremoto >= 5 and magnitud_terremoto < 6:
    print("fuerte(puede causar daños en estructuras débiles)")
elif magnitud_terremoto >= 6 and magnitud_terremoto < 7:
    print("muy fuerte(puede causar daño significativos)")
else:
    print("extremo(puede causar graves daño a gran escala)")

#10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
#si el usuario se encuentra en otoño, invierno, primavera o verano. 
hemisferio = input("en hemisferio te encuentras:(N/S)").upper()
if hemisferio == "N":
    print("se encuentra en el hemisferio norte")
elif hemisferio == "S":
    print("se encuentra en el hemisferio sur")

dia = int(input("ingrese el dia: "))
mes = int(input("ingrese el mes del 1 al 12: "))

if hemisferio == "N":
    if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20):
        print("invierno")
    elif (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20):
        print("primavera")
    elif (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20):
        print("verano")
    else:
        print("otoño")

elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20):
        print("Verano")
    elif (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20):
        print("Otoño")
    elif (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20):
        print("Invierno")
    else:
        print("Primavera")
else:
    print("Hemisferio inválido. Por favor, ingresa N o S.")


