from typing_extensions import Self
import numpy as np
import numpy

class ModeloSimplex():
    funcion_objetivo = np.array(float)
    n_variables = int
    n_restriccion = int
    restriccion = np.zeros(shape = (n_variables,n_restriccion))
    max = True
    """
    Esto es solo un maquetado del la case ModeloSimplex 

    Los métodos con return 0 modifican al objeto por lo 
    que la función final ya no debe retornar nada """

    def simplex_max():
        resultado = [[],[]]
        return resultado
    def simplex_min():
        resultado = [[],[]]
        return resultado
    def tableau_max(self):
        funcion_objetivo = numpy.multiply(funcion_objetivo,─1)
        restriccion
        return 0
    def tableau_min(self):
        funcion_objetivo
        restriccion
        return 0
    def columna_pivote_max(self):
        resultado = int
        return resultado
    def columna_pivote_min(self):
        resultado = int
        return resultado
    def fila_pivote(self):
        resultado = float
        return resultado
    def gauss(self,pivote_fila, pivote_columna):
        valor_pivote = Self.restriccion[pivote_fila][pivote_columna]
        for i in self.funcion_objetivo:
            self.restriccion[pivote_fila][i] = self.restriccion[pivote_fila][i]/valor_pivote
        return 0
    def parada_max(self):
        resultado = bool
        return resultado
    def parada_min(self):
        resultado = bool
        return resultado
