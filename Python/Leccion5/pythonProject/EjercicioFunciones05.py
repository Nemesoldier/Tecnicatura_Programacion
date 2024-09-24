# Ejercicio 5: Convertidor de temperaturas
# Realizar dos funciones para coomvertir de grados a celsius
# a fahrenheit y viceversa
# investigar las formulas

# Función para convertir de Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Función para convertir de Fahrenheit a Celsius
def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Solicitar la opción al usuario
opcion = input("Elija la conversión que desea realizar: \n1. Celsius a Fahrenheit \n2. Fahrenheit a Celsius \n")

if opcion == '1':
    celsius = float(input("Ingrese los grados Celsius: "))
    print(f"{celsius}°C son {celsius_a_fahrenheit(celsius):.2f}°F")
elif opcion == '2':
    fahrenheit = float(input("Ingrese los grados Fahrenheit: "))
    print(f"{fahrenheit}°F son {fahrenheit_a_celsius(fahrenheit):.2f}°C")
else:
    print("Opción no válida.")
