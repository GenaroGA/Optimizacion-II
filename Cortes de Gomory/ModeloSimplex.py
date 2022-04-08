from math import modf
import numpy as np

class ModeloSimplex():

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
        max_min = int(input("(1.-Max / 2.-Min?):"))
        if max_min == 1:
            self.max = True
        else:
            self.max = False

        #Se solicitan y almacenan los coeficientes de la FO en su forma estandar
        print("************************************************")
        print("*Digita los coeficientes de la función objetivo*")
        print("************************************************")
        for i in range (n_variables):
            self.funcion_objetivo[i] = input("x" + str(i+1) + " = ")
        

        """ 
        Se solicitan y almacenan los coeficientes de las ecuaciones
        que conforman las restricciones del modelo en su forma estandar
        """

        print("**********************************************")
        print("*Digita los coeficientes de las restricciones*")
        print("**********************************************")
        for i in range (n_restriccion):
            print("***Restricción " + str(i+1) + ":\n")
            for j in range (n_variables):
                self.restriccion[i][j] = input("x" + str(j+1) + " = ")
            self.restriccion[i][n_variables] = input("b" + str(i+1) + " = ")

        #Se establecen la variables básicas
        for i in range (n_restriccion):
            n = i
            self.variables_basicas_arr[i]=n+1


    def tableau(self):
        self.funcion_objetivo = np.multiply(self.funcion_objetivo,-1)
    def columna_pivote_max(self):
        resultado = np.argmin(self.funcion_objetivo)
        return resultado
    def columna_pivote_min(self):
        resultado = np.argmax(self.funcion_objetivo)
        return resultado
    def fila_pivote(self,pivote_columna):
        resultado = 1
        divisiones = np.zeros(shape=(0))
        for i in range(self.n_restriccion):
            if self.restriccion[i][pivote_columna] != 0:
                division = self.restriccion[i][self.n_variables]/self.restriccion[i][pivote_columna]
                divisiones = np.append(divisiones,division)
        resultado = np.argmin(divisiones)
        return resultado

    def variables_basicas(self,pivote_fila,pivote_columna):
        indice = np.where(self.variables_basicas_arr == pivote_fila+1)
        self.variables_basicas_arr[indice[0][0]] = pivote_columna+1

    def gauss(self,pivote_fila, pivote_columna):
        # Se ubica el elemento pivote
        valor_pivote = self.restriccion[pivote_fila][pivote_columna]

        # Se divide la fila pivote entre el elemento pivote
        for i in range(self.n_variables+1):
            self.restriccion[pivote_fila][i] = self.restriccion[pivote_fila][i]/valor_pivote

        # Se obtiene el elemento pivote de la fila
        aux = self.funcion_objetivo[pivote_columna]

        # Fila original - pivote de la fila * fila pivote
        for i in range(self.n_variables+1):
            self.funcion_objetivo[i] = self.funcion_objetivo[i] - (aux * self.restriccion[pivote_fila][i])
        for i in range(self.n_restriccion):
            # Se obtiene el elemento pivote de la fila
            aux = self.restriccion[i][pivote_columna]

            """
            Fila original - pivote de la fila * fila pivote 
            Exceptuando la fila pivote
            """
            for j in range(self.n_variables+1):
                if i != pivote_fila:
                    self.restriccion[i][j] = self.restriccion[i][j] - (aux * self.restriccion[pivote_fila][j])

    #Si hay valores negativos en la función objetivo entonces devuelve True
    def parada_max(self):
        resultado = False
        for i in range( len(self.funcion_objetivo) -1 ):
            if self.funcion_objetivo[i] < 0 :
                resultado=True; 
        return resultado
    #Si hay valores positivos en la función objetivo entonces devuelve True
    def parada_min(self):
        resultado = False
        for i in range( len(self.funcion_objetivo) -1 ):
            if self.funcion_objetivo[i] > 0 :
                resultado=True; 
        return resultado
    def corte_gomory(self):

        # Se busca el índice del resultado minimo del tableau optimo
        filas,columnas = self.restriccion.shape
        aux = np.zeros(shape=(0))
        for i in range (filas):
            aux = np.append(aux,self.restriccion[i][columnas-1])
        renglon_minimo = np.argmin(aux)

        # Se obtiene la parte entera y la parte fraccionaria del renglon seleccionado
        aux = np.zeros(shape=(0))
        # Se obtiene la parte entera de cada elemento del renglon pivote identificado y se calcula el renglon del corte
        for i in range (columnas):
            parte_decimal,parte_entera = modf(self.restriccion[renglon_minimo][i])
            if self.restriccion[renglon_minimo][i] > 0:
                aux = np.append(aux,-1 * parte_decimal)
            elif self.restriccion[renglon_minimo][i] < 0 :
                aux = np.append(aux,-1 - parte_decimal)
            else:
                aux = np.append(aux,0)


        # Se inserta una columna de ceros en el tableau y en el vector del corte (aux)

        #Se insertan ceros al final del arreglo y/o matriz
        
        ceros = np.zeros(shape=(filas,1))
        self.restriccion = np.append(self.restriccion, ceros, axis=1)
        self.funcion_objetivo = np.append(self.funcion_objetivo, 0)
        aux = np.append(aux, 1)

        #Se intercambia la ultima fila y la penultima para reacomodar el tableau
        #Matriz de restricciones 
        filas,columnas = self.restriccion.shape
        for i in range(filas):
            cambio = self.restriccion[i][columnas-1]
            self.restriccion[i][columnas-1] = self.restriccion[i][columnas-2]
            self.restriccion[i][columnas-2] = cambio
        #Arreglo de la función objetivo
        cambio = self.funcion_objetivo[len(self.funcion_objetivo)-1]
        self.funcion_objetivo[len(self.funcion_objetivo)-1] = self.funcion_objetivo[len(self.funcion_objetivo)-2]
        self.funcion_objetivo[len(self.funcion_objetivo)-2] = cambio
        #Arreglo del corte
        cambio = aux[len(aux)-1]
        aux[len(aux)-1] = aux[len(aux)-2]
        aux[len(aux)-2] = cambio

        #Se inserta el arreglo de corte a la matriz de restricciones
        self.restriccion = np.concatenate([self.restriccion,aux],axis=0)
        filas,columnas = self.restriccion.shape
        self.variables_basicas_arr = np.append(self.variables_basicas_arr,columnas)
        return renglon_minimo
    def columna_pivote_gomory(self, fila_pivote):
        resultado = 1
        columnas = self.funcion_objetivo.shape
        columnas = columnas[0]
        divisiones = np.zeros(shape=(0))
        for i in range(columnas-1):
            if self.restriccion[fila_pivote][i] != 0:
                division = self.funcion_objetivo[i]/self.restriccion[fila_pivote][i]
                if division < 0:
                    divisiones = np.append(divisiones,division)
                else:
                    divisiones = np.append(divisiones,-999)
            else:
                divisiones = np.append(divisiones,-999)
        resultado = np.argmax(divisiones)
        return resultado

    def parada_gomory(self):
        filas,columnas = self.restriccion.shape
        for i in range (columnas-1):
            if np.equal(np.mod(self.restriccion[filas-1][i],1),0):
                return False
            else:
                return True
