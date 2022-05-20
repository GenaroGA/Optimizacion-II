import numpy as np

class hungaro():
    def __init__(self):
        self.asignaciones = int(input("Numero de asignaciones: "))
        self.tabla = np.zeros(shape=(self.asignaciones,self.asignaciones))
        self.tabla_lineas = np.zeros(shape=(self.asignaciones,self.asignaciones))
        self.minFilas = []
        self.minColumnas = []
        self.cerosFilas = []
        self.cerosColumnas = []
        for i in range(self.asignaciones):
            for j in range(self.asignaciones):
                self.tabla[i][j] = float(input("Precio(" + str(i+1) + "," + str(j+1) + ") "))
    def minimos_filas(self):
        aux = []
        for i in range(self.asignaciones):
            for j in range(self.asignaciones):
                aux.append(self.tabla[i][j])
            self.minFilas.append(np.amin(aux))
    def minimos_columnas(self):
        aux = []
        for i in range(self.asignaciones):
            for j in range(self.asignaciones):
                aux.append(self.tabla[j][i])
            self.minColumnas.append(np.amin(aux))
    def restar_filas(self):
        for i in range(self.asignaciones):
            for j in range(self.asignaciones):
                self.tabla[i][j] = self.tabla[i][j] - self.minFilas[i]
    def restar_columnas(self):
        for i in range(self.asignaciones):
            for j in range(self.asignaciones):
                self.tabla[i][j] = self.tabla[i][j] - self.minColumnas[i]
    def contar_ceros(self):
        aux = []
        for i in range(self.asignaciones):
            for j in range(self.asignaciones):
                aux.append(self.tabla[i][j])
            self.cerosFilas = aux.count(0)
            aux = []
            for j in range(self.asignaciones):
                aux.append(self.tabla[j][i])
            self.cerosColumnas = aux.count(0)
    def lineas(self):
        if np.amax(self.cerosFilas) >= np.amax(self.cerosColumnas):
            indice = self.cerosFilas.index(np.amax(self.cerosFilas))
        for i in range(self.asignaciones):
            self.tabla[indice][i] = 999
        else:
            indice = self.cerosFilas.index(np.amax(self.cerosColumnas))
            self.tabla[indice][i] = 999
        for i in range(self.asignaciones):
            self.tabla_lineas[indice][i] = self.tabla_lineas[indice][i] + 1
