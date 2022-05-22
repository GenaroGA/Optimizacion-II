import numpy as np
import hungaro as h

tabla = h.hungaro()
print(tabla.tabla)
tabla.minimos_filas()
tabla.restar_filas()
print(tabla.tabla)
tabla.minimos_columnas()
tabla.restar_columnas()
print(tabla.tabla)

tabla.contar_ceros()
while np.amax(tabla.cerosFilas) > 0 and np.amax(tabla.cerosColumnas) > 0:
    tabla.lineas()
    print(tabla.tabla_lineas)
    tabla.contar_ceros()
print(tabla.tabla_restada)
tabla.asignacion()
print(tabla.tabla_asignaciones)
print(tabla.z)
