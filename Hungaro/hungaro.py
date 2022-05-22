import numpy as np

class hungaro():
    def __init__(self):
        self.asignaciones = 7 #int(input("Numero de asignaciones: "))
        self.tabla_original = np.array([[6,11,7,9,18,22,19],[25,18,19,9,7,25,14],[11,7,20,19,15,17,14],[23,19,8,13,15,6,5],[24,15,11,6,18,8,9],[7,22,13,7,24,14,12],[22,18,15,17,21,8,12]])#np.zeros(shape=(self.asignaciones,self.asignaciones))
        self.tabla = np.array([[6,11,7,9,18,22,19],[25,18,19,9,7,25,14],[11,7,20,19,15,17,14],[23,19,8,13,15,6,5],[24,15,11,6,18,8,9],[7,22,13,7,24,14,12],[22,18,15,17,21,8,12]])
        self.tabla_lineas = np.zeros(shape=(self.asignaciones,self.asignaciones))
        self.minFilas = []
        self.minColumnas = []
        self.cerosFilas = []
        self.cerosColumnas = []
        self.z = 0
        self.tabla_restada =  np.zeros(shape=(self.asignaciones,self.asignaciones))
        self.tabla_asignaciones = np.zeros(shape=(self.asignaciones,self.asignaciones))
        #for i in range(self.asignaciones):
        #    for j in range(self.asignaciones):
        #        self.tabla[i][j] = float(input("Precio(" + str(i+1) + "," + str(j+1) + ") "))
    def minimos_filas(self):
        for i in range(self.asignaciones):
            aux = []
            for j in range(self.asignaciones):
                aux.append(self.tabla[i][j])
            self.minFilas.append(np.amin(aux))
            self.z = self.z + np.amin(aux)
    def minimos_columnas(self):
        for i in range(self.asignaciones):
            aux = []
            for j in range(self.asignaciones):
                aux.append(self.tabla[j][i])
            self.minColumnas.append(np.amin(aux))
            self.z = self.z + np.amin(aux)
    def restar_filas(self):
        for i in range(self.asignaciones):
            for j in range(self.asignaciones):
                self.tabla[i][j] = self.tabla[i][j] - self.minFilas[i]
                self.tabla_restada[i][j] = self.tabla[i][j] 
    def restar_columnas(self):
        for i in range(self.asignaciones):
            for j in range(self.asignaciones):
                self.tabla[j][i] = self.tabla[j][i] - self.minColumnas[i]
                self.tabla_restada[j][i] = self.tabla[j][i] 
    def contar_ceros(self):
        self.cerosFilas = []
        self.cerosColumnas = []
        for i in range(self.asignaciones):
            aux = []
            for j in range(self.asignaciones):
                aux.append(self.tabla[i][j])
            self.cerosFilas.append(aux.count(0))
            aux = []
            for j in range(self.asignaciones):
                aux.append(self.tabla[j][i])
            self.cerosColumnas.append(aux.count(0))
    def lineas(self):
        if np.amax(self.cerosFilas) >= np.amax(self.cerosColumnas):
            indice = self.cerosFilas.index(np.amax(self.cerosFilas))
            for i in range(self.asignaciones):
                self.tabla[indice][i] = 999
                self.tabla_lineas[indice][i] = self.tabla_lineas[indice][i] + 1
                
        else:
            indice = self.cerosColumnas.index(np.amax(self.cerosColumnas))
            for i in range(self.asignaciones):
                self.tabla[i][indice] = 999
                self.tabla_lineas[i][indice] = self.tabla_lineas[i][indice] + 1
    def asignacion(self):
        for i in range(self.asignaciones):
            for j in range(self.asignaciones):
                if self.tabla_restada[i][j] == 0:
                    self.tabla_asignaciones[i][j] = self.tabla_original[i][j]
