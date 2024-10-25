import FieguraGeometrica
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo


print("Creacion de objeto clase Cuadrado".center(50, "_"))
cuadrado1 = Cuadrado(8, "Azul")
cuadrado1.alto = 7
#cuadrado1.ancho = 7
#print(cuadrado1.ancho)
#print(cuadrado1.alto)
print(f"Calculo del area del cuadrado: {cuadrado1.calcular_area()}")

#MRO = Metod Rsolusiton Order
#print(Cuadrado.mro())

print(cuadrado1)
print("Creacion de objeto clase Rectangulo".center(50,"_"))
rectangulo1 = Rectangulo(3, 9, "Verde")
rectangulo1.ancho = 8
print(f"Claculo del area del rectangulo: {rectangulo1.calcular_area()}")
print(rectangulo1)

#figura1 = FieguraGeometrica()  No se puede instanciar, es abstracta
print(Cuadrado.mro())