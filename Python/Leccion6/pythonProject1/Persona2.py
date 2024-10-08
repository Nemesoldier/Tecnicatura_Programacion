class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f"Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}")

    @property  # Decorador
    def nombre(self):  # Método Getter
        print("Estamos utilizando el método get")
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        print("Estamos utilizando el método set")
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def __del__(self):
        print(f"Persona2: {self._nombre} {self._apellido} {self._edad}")


if __name__ == "__main__":
    persona1 = Persona2("Ariel", "Betancud", 41)
    print(persona1.nombre)  # Llamamos al método getter
    persona1.mostrar_detalles()  # Llamamos al método para mostrar detalles
    persona1.nombre = "Juan Pedro"
    print(persona1.nombre) # Otra vez con el metodo getter
    print(persona1.mostrar_detalles())  # Llamammos el metodo mostrar detalles
    # Atributo read-only seria la edad porque no tiene el metodo set
    print(persona1.edad)
    # Tarea crear tres objetos mas utilizando los metodos getter and setter para modificar, y mostrar los cambios con el metodo mostrar detalles

    #Objeto numero 1
    persona2 = Persona2 ("Flor","Romero",23)
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    persona2.nombre = "Florencia"
    persona2.apellido = "Romery"
    persona2.edad = 22
    print(persona2.mostrar_detalles())

    #Objeto numero 2
    persona3 = Persona2("Caro","Felisa", 21)
    print(persona3.nombre)
    print(persona3.apellido)
    print(persona3.edad)
    persona3.nombre = "Carolina"
    persona3.apellido = "felix"
    persona3.edad = 31
    print(persona3.mostrar_detalles())

    #Objeto numero 3 de la tarea
    persona4 = Persona2("Naty","lucero",35)
    print(persona4.nombre)
    print(persona4.apellido)
    print(persona4.edad)
    persona4.nombre = "Natalia"
    persona4.apellido = "Lucero"
    persona4.edad = 33
    print(persona4.mostrar_detalles())

    print(__name__)









