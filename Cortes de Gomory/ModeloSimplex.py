from math import modf
import numpy as np

class ModeloSimplex():
    n_restriccion = 3
    n_variables = 3
    variables_basicas_arr = np.zeros(shape=(n_restriccion))
    funcion_objetivo = np.zeros(shape=(n_variables+1))
    restriccion = np.zeros(shape = (n_restriccion,n_variables+1))
    max = True
    """
    Esto es solo un maquetado del la case ModeloSimplex 
    Los métodos con return 0 modifican al objeto por lo 
    que la función final ya no debe retornar nada """

    def __init__(self,n_variables,n_restriccion):
        """ 
        Se guarda la cantidad de variables y restricciones
        del modelo
        """
        self.n_variables = n_variables
        self.n_restriccion = n_restriccion
        self.variables_basicas_arr = np.zeros(shape=(n_restriccion))
        self.funcion_objetivo = np.zeros(shape=(n_variables+1))
        self.restriccion = np.zeros(shape = (n_restriccion,n_variables+1))

        #Se determina si se va a maximizar o minimizar
        max_min = input("(1.-Max / 2.-Min?):")
        if max_min == 1:
            self.max = True
        else:
            self.max = False

        #Se solicitan y almacenan los coeficientes de la FO en su forma estandar
        print("************************************************")
        print("*Digita los coeficientes de la función objetivo*")
        print("************************************************")
        for i in range (n_variables):
            self.funcion_objetivo[i] = input("x" + str(i) + " = ")
        

        """ 
        Se solicitan y almacenan los coeficientes de las ecuaciones
        que conforman las restricciones del modelo en su forma estandar
        """

        print("**********************************************")
        print("*Digita los coeficientes de las restricciones*")
        print("**********************************************")
        for i in range (n_restriccion):
            print("***Restricción " + str(i) + ":\n")
            for j in range (n_variables):
                self.restriccion[i][j] = input("x" + str(j) + " = ")
            self.restriccion[i][n_variables] = input("b" + str(i) + " = ")

        #Se establecen la variables básicas
        for i in range (n_restriccion):
            self.variables_basicas_arr[i]=i+1


    def tableau(self):
        funcion_objetivo = np.multiply(funcion_objetivo,-1)
    def columna_pivote_max(self):
        resultado = int
        return resultado
    def columna_pivote_min(self):
        resultado = int
        return resultado
    def fila_pivote(self,pivote_columna):
        resultado = 1
        divisiones = np.zeros(shape=(0))
        for i in range(self.n_restriccion):
            if self.restriccion[i][self.n_variables+1] != 0:
                division = self.restriccion[i][self.n_variables+1]/self.restriccion[i][pivote_columna]
                divisiones = np.append(divisiones,division)
        resultado = list.index(min(divisiones))
        return resultado

    def variables_basicas(self,pivote_fila,pivote_columna):
        self.variables_basicas_arr[pivote_fila] = pivote_columna+1

    def gauss(self,pivote_fila, pivote_columna):
        # Se ubica el elemento pivote
        valor_pivote = self.restriccion[pivote_fila][pivote_columna]

        # Se divide la fila pivote entre el elemento pivote
        for i in range(self.n_variables):
            self.restriccion[pivote_fila][i] = self.restriccion[pivote_fila][i]/valor_pivote

        # Se obtiene el elemento pivote de la fila
        aux = self.funcion_objetivo[pivote_columna]

        # Fila original - pivote de la fila * fila pivote
        for i in range(self.n_variables):
            self.funcion_objetivo[i] = self.funcion_objetivo[i] - (aux * self.restriccion[pivote_fila][i])
        for i in range(self.n_variables):
            # Se obtiene el elemento pivote de la fila
            aux = self.restriccion[i][pivote_columna]

            """
            Fila original - pivote de la fila * fila pivote 
            Exceptuando la fila pivote
            """
            for j in range(self.n_restriccion):
                if i != pivote_fila:
                    self.restriccion[i][j] = self.restriccion[i][j] - (aux * self.restriccion[pivote_fila][i])


    def parada_max(self):
        resultado = False
        for i in range( len(self.funcion__objetivo) ):
            if self.funcion__objetivo[i] < 0 :
                resultado=True; 
        return resultado
    def parada_min(self):
        resultado = False
        for i in range( len(self.funcion__objetivo) ):
            if self.funcion__objetivo[i] > 0 :
                resultado=True; 
        return resultado
    def corte_gomory(self):

        # Se busca el índice del resultado minimo del tableau optimo

        aux = np.zeros(shape=(self.n_restriccion))
        for i in range (self.n_restriccion):
            aux[i] = self.restriccion[i][self.n_restriccion]
        renglon_minimo = list.index(min(aux))

        # Se obtiene la parte entera y la parte fraccionaria del renglon seleccionado
        aux = np.zeros(shape=(self.n_variables+1))
        # Se obtiene la parte entera de cada elemento del renglon pivote identificado y se calcula el renglon del corte
        for i in range (self.n_variables+1):
            parte_entera,parte_entera = modf(self.restriccion[renglon_minimo][i])
            aux[i] = parte_entera - self.restriccion[renglon_minimo][i]


        # Se inserta una columna de ceros en el tableau y en el vector del corte (aux)

        #Se insertan ceros al final del arreglo y/o matriz
        ceros = np.zeros(shape=(self.n_restriccion,1))
        self.restriccion = np.append(self.restriccion, ceros, axis=1)
        self.funcion_objetivo = np.append(self.funcion_objetivo, 0)
        aux = np.append(aux, 1)

        #Se intercambia la ultima fila y la penultima para reacomodar el tableau
        #Matriz de restricciones 
        for i in range(self.n_restriccion):
            cambio = self.restriccion[i][len(self.restriccion)]
            self.restriccion[i][len(self.restriccion)] = self.restriccion[i][len(self.restriccion)-1]
            self.restriccion[i][len(self.restriccion)-1] = cambio
        #Arreglo de la función objetivo
        cambio = self.funcion_objetivo[len(self.funcion_objetivo)]
        self.funcion_objetivo[len(self.funcion_objetivo)] = self.funcion_objetivo[len(self.funcion_objetivo)-1]
        self.funcion_objetivo[len(self.funcion_objetivo)-1] = cambio
        #Arreglo del corte
        cambio = aux[len(self.aux)]
        aux[len(self.aux)] = self.aux[len(self.aux)-1]
        aux[len(self.aux)-1] = cambio

        #Se inserta el arreglo de corte a la matriz de restricciones
        self.restriccion = np.vstack([self.restriccion,aux])
        return renglon_minimo
    def columna_pivote_gomory(self, fila_pivote):
        resultado = 1
        divisiones = np.zeros(shape=(0))
        for i in range(len(self.funcion_objetivo)):
            if self.restriccion[fila_pivote][i] != 0:
                division = abs(self.funcion_objetivo[i]/self.restriccion[fila_pivote][i])
                divisiones = np.append(divisiones,division)
        resultado = list.index(min(divisiones))
        return resultado
