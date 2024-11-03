class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, other): # other sigifica otro
        return f"{self.nombre} + {other.nombre}"

    def __sub__(self, otro): # Sub sifnifica substraction
        return self.edad - otro.edad


persona1 = Persona("Ariel", 40)
persona2 = Persona("Betancud",5)

#person1.__add__(persona2) Sintaxis interna y automatica

print(persona1 + persona2)
print(persona1 - persona2)



