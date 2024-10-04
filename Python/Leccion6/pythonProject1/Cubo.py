"""
Crear la clase Cubo con los atributos, ancho, alto y profundidad, con un metodo calcular_volumen que tendra la formula:
volumen = ancho * altura * profundidad, que el usuario ingrese los valores

"""
class Cubo:
    def __init__(self, ancho, alto, profundidad):
        self.ancho = ancho
        self.alto = alto
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.ancho * self.alto * self.profundidad

# Ingresar los valores de ancho, alto y profundidad por el usuario
ancho = int(input("Ingrese el ancho del cubo: "))
alto = int(input("Ingrese el alto del cubo: "))
profundidad = int(input("Ingrese la profundidad del cubo: "))

# Crear un objeto de la clase Cubo
cubo = Cubo(ancho, alto, profundidad)

# Calcular y mostrar el volumen
volumen = cubo.calcular_volumen()
print(f"El volumen del cubo es: {volumen}")
