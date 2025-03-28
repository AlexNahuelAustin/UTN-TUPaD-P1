#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.  
print("hola mundo!")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir 
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para 
# realizar la impresión por pantalla. 
nombre=input("ingrese su nombre: ")
print(f"hola {nombre}!")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar 
# la impresión por pantalla. 
nombre=input("ingrese tu nombre completo ")
apellido=input("ingrese su apellido: ")
edad=input("ingrese su edad: ")
LugarResidencia=input("ingrese su lugar de residencia actual: ")
print(f"soy {nombre} {apellido}, tengo {edad} y vivo {LugarResidencia} ")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
# su perímetro. 
radio=float(input("ingrese el radio: "))
import math
area= math.pi *radio**2
print("el area de circulo es: ", area)

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
#cuántas horas equivale.
segundo_ingresados=int(input("ingrese la cantidad de segundo: "))
horas=segundo_ingresados/3600
print("la cantidad de segundo "+ str(segundo_ingresados)+ " es en horas: "+ str(horas))

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
#multiplicar de dicho número.  
numero=int(input("ingrese un numero: "))
print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. 

numero1=int(input("ingrese el primer numero: "))
numero2=int(input("ingrese el segundo numero: "))
suma=numero1+numero2
resta=numero1-numero2
multiplicacion=numero1*numero2
division=numero1/numero2
print(f"la suma de ambos es {suma}, la resta de ambos numero es {resta}, la multiplicacion es {multiplicacion} y la division es {division} ")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente 
#modo:  
#��𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)2

altura=float(input("ingrese su altura: "))
peso=float(input("ingrese su peso: "))
IMC=peso/altura**2
print("su indice de masa corporal(IMC) es: "+ str(IMC))

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: 
#t𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5*𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠   + 32
celsius=float(input("ingrese la temperatura en grados celsius: "))
𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡=9/5*celsius+32
print(f"la temperatura en 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 es {Fahrenheit}")

#10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de 
# dichos números. 
numero1=int(input("ingrese el primer numero "))
numero2=int(input("ingrese el segundo numero "))
numero3=int(input("ingrese el tercer numero "))
promedio=(numero1+numero2+numero3)/3
print("el promedio de los 3 numeros ingresado es: ", promedio)