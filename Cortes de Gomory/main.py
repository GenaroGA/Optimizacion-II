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

parada = True
while parada:
    c_pivote = modelo.columna_pivote_max()
    f_pivote = modelo.fila_pivote(c_pivote)
    modelo.variables_basicas(f_pivote,c_pivote)
    modelo.gauss(f_pivote,c_pivote)
    print(modelo.funcion_objetivo)
    print(modelo.restriccion)
    parada = modelo.parada_max()
parada = True

while parada:
    
    f_pivote = modelo.corte_gomory()
    c_pivote = modelo.columna_pivote_gomory(f_pivote)

    modelo.gauss(f_pivote,c_pivote)
    print(modelo.funcion_objetivo)
    print(modelo.restriccion)
    parada = modelo.parada_gomory()

