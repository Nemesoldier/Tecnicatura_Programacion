
"""print("Verificamos si el año es bisiesto:")
print("")
opcion = 0
while opcion != 1:
    num = int(input("Ingrese el año: "))
    if (num % 4 == 0 and num % 100 != 0) or (num % 400 == 0):
        print("El año es bisiesto")
    else:
        print("El año no es bisiesto")
    opcion = int(input("Para finalizar digite 1, para seguir digite 0: "))
print("Finalizó el programa")"""

"""n = int(input("Digite la cantidad de numeros a sumarse:"))
suma = 0
for i in range (1,n+1):
    suma += i
print(f"la suma es:{suma}")"""

"""calificacion_b = float('inf')
calificacion_p = 0
suma = 0


for i in range(10):
    calificacion = float(input("Digite una nota: "))
    suma += calificacion


    if calificacion < calificacion_b:
        calificacion_b = calificacion


calificacion_p = suma / 10


print("La nota promedio es:", calificacion_p)
print("La calificación más baja es:", calificacion_b)
"""

"""conteo_p = 0
conteo_neg = 0
conteo_neu = 0
for i in range(10):
    num = int(input("Digite un numero: "))
    if num == 0:
        conteo_neu += 1
    elif num > 0:
        conteo_p += 1
    elif num < 0:
        conteo_neg += 1
print(f"Los numeros positivos son: {conteo_p}")
print(f"Los numeros negativos son: {conteo_neg}")
print(f"Los numeros neutros son: {conteo_neu}")
"""

"""num = int(input("Digite un numero: "))
if num < 0:
    factorial = "Ingresa un numero positivo:"
else:
    factorial = 1
    for i in range(1,num +1):
        factorial *= i
print("El factorial es: ",factorial)"""


"""suma_p = 0
conteo_p = 0
suma_i = 0
conteo_i = 0

numeros = int(input("Digite la cantidad de numeros a ingresar: "))
for i in range(numeros):
    num = int(input(f"Digite un numero ({i + 1}): "))
    if num % 2 == 0:
        suma_p += num
        conteo_p += 1
    else:
        suma_i += num
        conteo_i += 1
if conteo_p == 0:
    print("No hay numeros pares.")
else:
    print(f"La suma de los numeros pares es: {suma_p}")
    print(f"El conteo de los numeros pares es: {conteo_p}")
if conteo_i == 0:
    print("No hay numeros impares.")
else:
    promedio_i = suma_i / conteo_i
    print(f"El promedio de los numeros imapres es: {promedio_i:.2}")
"""
suma = 0
for i in range(1, 6):
    print(f"El salario para el empleado {i}:")
    tarifa = float(input("Digite la tarifa por hora trabajada: "))
    horas = float(input("Digite las horas trabajadas: "))
    salario = horas * tarifa
    print(f"El sueldo es: {salario}")
    suma += salario

print("La suma de todos los sueldos es:", suma)




