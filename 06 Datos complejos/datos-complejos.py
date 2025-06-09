#1) Dado el diccionario precios_frutas
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
#1450}
#Añadir las siguientes frutas con sus respectivos precios:
##● Naranja = 1200
#● Manzana = 1500
#● Pera = 2300

precio_frutas = {
'banana': 1200,
'anana': 2500,
'melon' : 3000,
'uva':1450    
}

precio_frutas['naranja'] = 1200
precio_frutas['manzana'] = 1500
precio_frutas['pera'] = 1450

print(precio_frutas)

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
#● Banana = 1330
#● Manzana = 1700
#● Melón = 2800


precio_frutas = {
'banana': 1200,
'anana': 2500,
'melon' : 3000,
'uva':1450    
}

precio_frutas['naranja'] = 1200
precio_frutas['manzana'] = 1500
precio_frutas['pera'] = 1450

print(precio_frutas)

precio_frutas['banana'] = 1330
precio_frutas['manzana'] = 1700
precio_frutas['melon'] = 2800

print(precio_frutas)


#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
#precios.

precio_frutas = {
'banana': 1200,
'anana': 2500,
'melon' : 3000,
'uva':1450    
}

precio_frutas['naranja'] = 1200
precio_frutas['manzana'] = 1500
precio_frutas['pera'] = 1450

print(precio_frutas)

precio_frutas['banana'] = 1330
precio_frutas['manzana'] = 1700
precio_frutas['melon'] = 2800

print(precio_frutas)

print(list(precio_frutas))

#4) Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe.

guia_telefonica ={
'alex': 879252,
'esteban':56402455,
'carla': 1475548,
'lunsa': 66872208,
'john': 25880456
}

salida_de_la_guia = True

while salida_de_la_guia:
    print("ingrese el nombre para buscar su numero telefonico\n escriba 'salir' para terminar la busqueda ")
    nombre_buscado = input("Nombre: ").lower()
    
    if nombre_buscado == 'salir':
        print("saliendo de la guia")
        salida_de_la_guia = False
    
    elif nombre_buscado in guia_telefonica:
        numero_telefonico = guia_telefonica[nombre_buscado]
        print(f"el numero de {nombre_buscado.capitalize()} es: {numero_telefonico} ")
        salida_de_la_guia = False
    else:
        print(f"el nombre {nombre_buscado.capitalize()} no se encuentra en la guia. Intente con otro nombre")

#5)Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra.


frase = input("Ingrese una frase: ")

palabras = frase.lower().split()

palabras_unicas = set(palabras)

conteo = {
    
}

for palabra in palabras:
    if palabra in conteo:
        conteo[palabra] += 1
    else:
        conteo[palabra] = 1

print(f"\nLa frase es: {frase}")
print(f"\nPalabras únicas: {palabras_unicas}")
print(f"\nConteo de palabras: {conteo}")

#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#Luego, mostrá el promedio de cada alumno.

alumnos_notas ={
    
}

for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    notas = input(f"Ingrese 3 notas separadas por espacios para {nombre}: ")
    notas = tuple(map(float, notas.split()))
    alumnos_notas[nombre] = notas
    
    print(alumnos_notas)
    
    for nombre,notas in alumnos_notas.items():
        promedio = sum(notas)/len(notas)
        print(f"el promedio de {nombre} es: {promedio:2f}")
        
#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
#• Mostrá los que aprobaron ambos parciales.
#• Mostrá los que aprobaron solo uno de los dos.
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial_1 = {'juan', 'pedro','matias','sofia','lucia','ethian','luan','ludmila','federico'}
parcial_2 = {'luan','luz','matias','jorge','ethian','john','park','federico','pedro','goro'}

aprobaron_ambos = parcial_1.intersection((parcial_2))

print("los estudiante que aprobaron ambos parcial fueron", aprobaron_ambos)


aprobaron_solo_uno = parcial_1.symmetric_difference(parcial_2)

print("aprobaron solo uno de los parciales ", aprobaron_solo_uno)


aprobaron_al_menos_uno = parcial_1.union(parcial_2)

print("aprbaron solo al menos 1", aprobaron_al_menos_uno)

#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe.

stock_guitarras = {
'fender(electrica)' : 5,
'gibson(electrica)': 2,
'epiphone(electrica)': 4,
'squier(electrica)': 'AGOTADA',
'taylor(acustica)' : 10,
'takamine' : 'AGOTADA', 
}
#• Consultar el stock de un producto ingresado.
print(stock_guitarras['fender(electrica)'])

#• Agregar unidades al stock si el producto ya existe.
stock_guitarras['squier(electrica)'] = 6
print(stock_guitarras['squier(electrica)'])

#• Agregar un nuevo producto si no existe.
stock_guitarras['martin(acustica)'] = 1
stock_guitarras['jackson(electrica)'] = 8

print(stock_guitarras['martin(acustica)'])
print(stock_guitarras['jackson(electrica)'])

#todas las guitarras
print(stock_guitarras)

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
#Permití consultar qué actividad hay en cierto día y hora.


agenda = {
('lunes', '9:25'): 'salir a correr',
('lunes', '12:00'): 'hacer las compras',
('lunes', '15:00'): 'clase de anatomia',
('lunes','17:00'): 'estudiar anatomia',
('martes', '8:30'): 'clase de fisiologia',
('martes', '15:00'): 'estudiar fisiologia',
('viernes','9:25'): 'ir al gimnasio',
('viernes', '15:00'): 'presentar el trabajo de bioquimica'  
}


print(agenda[('lunes', '15:00')])

#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
#diccionario donde:
#• Las capitales sean las claves.
#• Los países sean los valores.

capitales = {
'buenos aires': 'argentina',
'paris': 'francia',
'tokio': 'japon',
'berlin': 'alemania',
'madrid': 'españa',
'seul': 'corea del sur',
'Nursultán': 'Kazajistán',
'Yamusukro': 'Costa de Marfil',
'Baku': 'Azerbaiyán',
'lisboa': 'portugal',
}


print(capitales['Baku'])
print(capitales)