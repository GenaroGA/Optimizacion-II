import numpy as np

class hungaro():
    def __init__(self):
        # Determina el número de filas y columnas de la tabla
        self.asignaciones = 7 #int(input("Numero de asignaciones: ")) 
        # Se guardan los costos entre cada uno de las asignaciones en dos matrices 
        # En una se haran todas las operaciones y en la otra se usará mas tarde para las asignaciones
        self.tabla_original = np.array([[6,11,7,9,18,22,19],[25,18,19,9,7,25,14],[11,7,20,19,15,17,14],[23,19,8,13,15,6,5],[24,15,11,6,18,8,9],[7,22,13,7,24,14,12],[22,18,15,17,21,8,12]])#np.zeros(shape=(self.asignaciones,self.asignaciones))
        self.tabla = np.array([[6,11,7,9,18,22,19],[25,18,19,9,7,25,14],[11,7,20,19,15,17,14],[23,19,8,13,15,6,5],[24,15,11,6,18,8,9],[7,22,13,7,24,14,12],[22,18,15,17,21,8,12]])
        # Se define una matriz de ceros del tamaño de la original para dibujar las lineas posteriormente
        self.tabla_lineas = np.zeros(shape=(self.asignaciones,self.asignaciones))
        # Se define una matriz donde de almacenarán los valores minimos de cada fila
        self.minFilas = []
        # Se define una matriz donde de almacenarán los valores minimos de cada columna
        self.minColumnas = []
        # Se almacenan la cantidad de ceros que hay por fila
        self.cerosFilas = []
        # Se almacenan la cantidad de ceros que hay por columna
        self.cerosColumnas = []
        # Se define la variable donde se guardara el valor de la FO
        self.z = 0
        # Se crea una matriz donde se guardará la matiz resultante de restar los valores minimos por filas y columna
        self.tabla_restada =  np.zeros(shape=(self.asignaciones,self.asignaciones))
        # Se crea una matriz donde se mostrarán las posibles asignaciones
        self.tabla_asignaciones = np.zeros(shape=(self.asignaciones,self.asignaciones))
        #for i in range(self.asignaciones):
        #    for j in range(self.asignaciones):
        #        self.tabla[i][j] = float(input("Precio(" + str(i+1) + "," + str(j+1) + ") "))
    def minimos_filas(self):
        for i in range(self.asignaciones):
            aux = [] # Arreglo auxiliar donde se irán copiando cada fila o columna 
            for j in range(self.asignaciones):
                aux.append(self.tabla[i][j]) 
                # Se agregan los valores minimos de cada fila
            self.minFilas.append(np.amin(aux))
            # Se suman los valores minimos de cada fila en la FO
            self.z = self.z + np.amin(aux)
    def minimos_columnas(self):
        for i in range(self.asignaciones):
            aux = [] # Arreglo auxiliar donde se irán copiando cada fila o columna 
            for j in range(self.asignaciones):
                aux.append(self.tabla[j][i])
                # Se agregan los valores minimos de cada fila
            self.minColumnas.append(np.amin(aux))
            # Se suman los valores minimos de cada fila en la FO
            self.z = self.z + np.amin(aux)
    def restar_filas(self):
        for i in range(self.asignaciones):
            for j in range(self.asignaciones):
                # Se resta el valor minimo de cada fila a la tabla 
                self.tabla[i][j] = self.tabla[i][j] - self.minFilas[i]
                # Se guardan los valores restados en la tabla restada
                self.tabla_restada[i][j] = self.tabla[i][j] 
    def restar_columnas(self):
        for i in range(self.asignaciones):
            for j in range(self.asignaciones):
                # Se resta el valor minimo de cada columna a la tabla 
                self.tabla[j][i] = self.tabla[j][i] - self.minColumnas[i]
                # Se guardan los valores restados en la tabla restada
                self.tabla_restada[j][i] = self.tabla[j][i] 
    def contar_ceros(self):
        # Se restean los arreglos donde se almacenan la cantidad de ceros de cada fila y columna
        self.cerosFilas = []
        self.cerosColumnas = []
        for i in range(self.asignaciones):
            # Se compian los valores de cada fila a un arreglo
            aux = []
            for j in range(self.asignaciones):
                aux.append(self.tabla[i][j])
            # Se inserta en el arreglo cerosFilas la cantidad de ceros que hay en el arreglo aux
            self.cerosFilas.append(aux.count(0))
            # Se resetea el arreglo auxiliar
            aux = []
            # Se compian los valores de cada columna a un arreglo
            for j in range(self.asignaciones):
                aux.append(self.tabla[j][i])
            # Se inserta en el arreglo cerosColumnas la cantidad de ceros que hay en el arreglo aux
            self.cerosColumnas.append(aux.count(0))
    def lineas(self):
        # Si el valor máximo del arreglo cerosFila es mayor que el de cerosColumnas
        if np.amax(self.cerosFilas) >= np.amax(self.cerosColumnas):
            # Se guarda el índice de la fila donde hay más ceros
            indice = self.cerosFilas.index(np.amax(self.cerosFilas))
            # Se sustituyen los valores de la fila por 999 y se suma 1 a la fila donde se dibuja una linea en el arreglo tabla_lineas
            for i in range(self.asignaciones):
                self.tabla[indice][i] = 999
                self.tabla_lineas[indice][i] = self.tabla_lineas[indice][i] + 1
                
        else:
            # Se guarda el índice de la fila donde hay más ceros
            indice = self.cerosColumnas.index(np.amax(self.cerosColumnas))
            for i in range(self.asignaciones):
                # Se sustituyen los valores de la columna por 999 
                # Se suma 1 a la columna donde se dibuja una linea en el arreglo tabla_lineas
                self.tabla[i][indice] = 999
                self.tabla_lineas[i][indice] = self.tabla_lineas[i][indice] + 1
    def asignacion(self):
        for i in range(self.asignaciones):
            for j in range(self.asignaciones):
                if self.tabla_restada[i][j] == 0:
                    self.tabla_asignaciones[i][j] = self.tabla_original[i][j]
