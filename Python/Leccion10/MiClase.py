class MiClase:
    # Variable de clase, este atributo da a cada objeto el mismo valor
    variable_clase = "Esta es una variable de clase"

    def __init__(self, variable_instancia):  # La variable de instancia, da diferentes valores
        self.variable_instancia = variable_instancia  # Arreglado: variable de instancia separada


print(MiClase.variable_clase)  # Imprime la variable de clase
miClase1 = MiClase("Esta es una variable de instancia")
print(miClase1.variable_instancia)  # Correcto: imprime la variable de instancia
print(miClase1.variable_clase)  # Imprime la variable de clase
miClase2 = MiClase("Esta es otra prueba de variable de instancia")
print(miClase2.variable_instancia)  # Imprime la variable de instancia
print(miClase2.variable_clase)  # Imprime la variable de clase

