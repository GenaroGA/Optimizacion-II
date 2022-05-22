import numpy as np
import hungaro as h

tabla = h.hungaro() # Se crea la clase 
print(tabla.tabla)
tabla.minimos_filas() # Se obtienen los números minimos de cada fila
tabla.restar_filas() # Se restan las filas con los números mínimos
print(tabla.tabla) 
tabla.minimos_columnas() # Se obtienen los números minimos de cada columna
tabla.restar_columnas() # Se restan las columnas con los numeros minimos
print(tabla.tabla)

tabla.contar_ceros() # Se cuentan los ceros
# El ciclo se ejecuta mientras el máximo de cada fila y columna sea mayor a cero
while np.amax(tabla.cerosFilas) > 0 and np.amax(tabla.cerosColumnas) > 0: 
    # En una tabla de ceros de suma un 1 a la fila o columna con el máximo número de ceros y se sustituyen los valores de la tabla original por un valor muy grande
    tabla.lineas() 
    print(tabla.tabla_lineas)
    tabla.contar_ceros() # Se vuelven a contar los ceros por fila y columna
print(tabla.tabla_restada)
tabla.asignacion() # Se crea una tabla con los valores que se hicieron 0 dejando su costo
print(tabla.tabla_asignaciones)
print(tabla.z) 
