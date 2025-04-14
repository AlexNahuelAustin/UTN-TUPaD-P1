#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for numero in range(101):  
    print(numero)


#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

num = int (input("ingrese un numero: "))
num_dig = 0

while num > 0:
    num = num // 10 
    num_dig += 1

print("la cantidad de digitos es: ", num_dig)




#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.
valor1 = int(input("Ingrese el primer valor entero: "))
valor2 = int(input("Ingrese el segundo valor entero: "))

suma = 0

if valor1 < valor2:
    for numero in range(valor1 + 1, valor2):
        suma += numero
elif valor2 < valor1:
    for numero in range(valor2 + 1, valor1):
        suma += numero
else:
    print("Los valores ingresados son iguales, no hay números entre ellos.")

if valor1 != valor2:
    print(f"La suma de los números entre {valor1} y {valor2}  es: {suma}")

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.
suma_total = 0
cont = 1

while True:
    numero = int(input(f"Ingrese el número {cont} (ingrese 0 para detener): "))
    if numero == 0:
        break
    suma_total += numero
    cont += 1

print(f"El total acumulado es: {suma_total}")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random

numero_aleatorio = random.randint(0, 9)
intentos = 0

while True:
    intento = int(input("Adivina el número (entre 0 y 9): "))
    intentos += 1
    if intento == numero_aleatorio:
        print(f"¡Correcto! Adivinaste el número en {intentos} intentos.")
        break
    elif intento < numero_aleatorio:
        print("El número es mayor.")
    else:
        print("El número es menor.")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.
for num in range(100, -1, -2):
    print(num)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.
limite = int(input("Ingrese un número entero positivo: "))
suma = 0
for num in range(limite + 1):
    suma += num
print(f"La suma de los números desde 0 hasta {limite} es: {suma}")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).
cantidad_num = 100 
pares = 0
impares = 0
negativos = 0
positivos = 0

print(f"Ingrese {cantidad_num} números enteros:")
for i in range(cantidad_num):
    numero = int(input(f"Número {i + 1}: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero < 0:
        negativos += 1
    elif numero > 0:
        positivos += 1

print(f"\nCantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números negativos: {negativos}")
print(f"Cantidad de números positivos: {positivos}")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).
cantidad_num = 100
suma_total = 0

print(f"Ingrese {cantidad_num} números enteros:")
for i in range(cantidad_num):
    numero = int(input(f"Número {i + 1}: "))
    suma_total += numero

if cantidad_num > 0:
    media = suma_total / cantidad_num
    print(f"\nLa media de los números ingresados es: {media}")
else:
    print("No se ingresaron números para calcular la media.")


#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
num_str = input("Ingrese un número entero: ")
num_invertido_str = num_str[::-1]
print(f"El número invertido es: {num_invertido_str}")