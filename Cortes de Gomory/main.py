import ModeloSimplex as MS

# TODO Crear un metodo para ingresar el Tableau de una hoja de excel

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
if modelo.max == True:
    while parada:
        c_pivote = modelo.columna_pivote_max()
        f_pivote = modelo.fila_pivote(c_pivote)
        modelo.variables_basicas(f_pivote,c_pivote)
        modelo.gauss(f_pivote,c_pivote)
        print(modelo.funcion_objetivo)
        print(modelo.restriccion)
        print("*******************")
        print("*Variables Básicas*")
        print("*******************")
        print(modelo.variables_basicas_arr)
        parada = modelo.parada_max()
else:
    while parada:
        c_pivote = modelo.columna_pivote_min()
        f_pivote = modelo.fila_pivote(c_pivote)
        modelo.variables_basicas(f_pivote,c_pivote)
        modelo.gauss(f_pivote,c_pivote)
        print(modelo.funcion_objetivo)
        print(modelo.restriccion)
        print("*******************")
        print("*Variables Básicas*")
        print("*******************")
        print(modelo.variables_basicas_arr)
        parada = modelo.parada_min()

parada = True

 #  TODO meter el procedimiento en un while
    
f_pivote = modelo.corte_gomory()
c_pivote = modelo.columna_pivote_gomory(f_pivote)
f_pivote = len(modelo.restriccion)-1
modelo.variables_basicas(f_pivote,c_pivote)
modelo.gauss(f_pivote,c_pivote)
print(modelo.funcion_objetivo)
print(modelo.restriccion)
parada = modelo.parada_gomory()

