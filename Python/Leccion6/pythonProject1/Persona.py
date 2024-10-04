class Persona:  #Creamos una clase
    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs):  #Se lo llama como Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni # Este atributo esta encapsulado de una manera sugerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalle(self):
        print(f"La clase persona tiene los siguientes datos:  {self.nombre} {self.apellido} {self._dni} {self.edad}, la direccion es: {self.args}, los datos importantes son: {self.kwargs}")



persona1 = Persona("Ariel", "Betancud", 403213312, 40)  #Necesitamos enviar argumentos
#print(persona1.nombre)
#print(persona1.apellido)
#print(persona1.edad)
print(f"El objeto1  de la clase persona: {persona1.nombre} {persona1.apellido} su edad es:  {persona1.edad}")
persona2 = Persona("Osvaldo", "Giordadnini", 45323123, 45)
print(f"El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} su edad es:  {persona2.edad}")

persona1.nombre = "Liliana"
persona1.apellido = "Bucella"
persona1.edad = 48
print(f"El objeto 1 modificado de la clase persona: {persona1.nombre} {persona1.apellido} su edad es:  {persona1.edad}")

#Los atributos son: Caracteristiocas
# Los metododos son: el comportamiento que van a tener los objetos (acciones)
persona1.mostrar_detalle() #la referencia en este caso se pasa de manera automatica
persona2.mostrar_detalle()

# Persona.mostrar_detalle(persona1) # Debemos pasarle una referencia para el self o dara error
persona1.telefono = "44424223232"
print(f"Este es el telefono de: {persona1.nombre} {persona1.telefono}") # Cremos un atributo de un objeto

# print(persona2.telefono) El objeto persona2 no tiene este atributo, da error
persona3 = Persona("Rogelio", "Romero", 23323213123, 23, "Manzana", 77, "Casa", 18, Altura = 1.83, Peso = 105, Cfacorito = "Azul", Auto = "Citroen", modelo = 2021)
persona3.mostrar_detalle()
# print(persona3._dni) # Esto no se debe utilizar (esta encaptuslado) esto dice que lo desconocemos python
#persona3.__nombre  # Esta totalmente encapsulado