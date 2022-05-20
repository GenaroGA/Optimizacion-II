import numpy as np
import hungaro as h

tabla = h.hungaro()
print(tabla.tabla)
tabla.minimos_filas()
tabla.restar_filas()
print(tabla.tabla)
tabla.minimos_columnas()
tabla.restar_columnas()

tabla.contar_ceros()
while np.amax(tabla.cerosFilas) > 0 and np.amax(tabla.cerosColumnas) > 0:
    tabla.contar_ceros()
    tabla.lineas()
    print(tabla.tabla_lineas)
print(tabla.tabla)
