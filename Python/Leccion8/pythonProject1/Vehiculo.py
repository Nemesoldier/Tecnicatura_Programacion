
"""
Definir una clase padre llamada Vehiculo y dos clases hijas llamadas Auto y Bicicleta, las cuales heredan de la clase padre
vehiculo. La clase padre debe tener los siguientes atributos y metodos:
Vehiculo (clase padre)
-Atrributos (color, ruedas)
-Metodos (__init__)( y __str__())

Auto (clase hija del vehiculo)
-Atributos(velocidad (km/hr))
-metodos (__init__) color, ruedas, velocidad( y __str())

bicicleta(clase hija de vehiculo)
-Atributos(tipo(urbana/montaña/etc.)
metodos (__init(color, ruedas, tipo) y __str()

Crar un objeto de cada clase
"""
# Clase padre Vehiculo
class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f'Vehículo [Color: {self.color}, Ruedas: {self.ruedas}]'


# Clase hija Auto
class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return f'Auto [Color: {self.color}, Ruedas: {self.ruedas}, Velocidad: {self.velocidad} km/h]'


# Clase hija Bicicleta
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f'Bicicleta [Color: {self.color}, Ruedas: {self.ruedas}, Tipo: {self.tipo}]'


# Crear un objeto de cada clase
vehiculo1 = Vehiculo("Rojo", 4)
auto1 = Auto("Azul", 4, 180)
bicicleta1 = Bicicleta("Verde", 2, "Montaña")

# Imprimir los objetos
print(vehiculo1)
print(auto1)
print(bicicleta1)



