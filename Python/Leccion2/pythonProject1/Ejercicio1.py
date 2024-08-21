"""
Ejercicio 1, plasmar la expresion en una expresion algoritmica, pasarla a codigo
"""
"""
a = float(input("Digite el valor de a: "))
b = float(input("Digite el valor de b: "))
c = float(input("Digite el calor de c: "))
resultado = (a ** 3 * (b ** 2 - 2 * a * c)) / (2 * b)
print(f"El resultado es: {resultado} ")
"""


"""
condicion = False
#if condicion:
#    print("La condicion es verdadera")
#else:
#    print("La condicion es falsa")
print ("Condicion verdadera") if condicion else print("Condicion Falsa") #(Recomendable cuando el codigo es pequeño)
"""

n = int(input("Digite numero de estaciones del 1 al 12: "))
if n <= 3:
    print("Verano")
elif n <= 6:
    print("Otoño")
elif n <= 9:
    print("Invierno")
elif n <= 12:
    print("Primavera")
else:
    print("Digite un numero menor a 12")
