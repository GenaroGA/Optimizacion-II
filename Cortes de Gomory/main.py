from numpy import int32
import ModeloSimplex as MS

variables = int(input("Variables = "))
restricciones = int(input("Restricciones = "))

modelo = MS.ModeloSimplex(variables,restricciones)
modelo.tableau()
print("*****************")
print("*Tableau Inicial*")
print("*****************")
print(modelo.funcion_objetivo)
print(modelo.restriccion)

