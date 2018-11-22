import numpy as np


class Resultado:
    def __init__(self, cadA, cadB, pasos, tiempo, hipA, hipB):
        self.cadA = cadA
        self.cadB = cadB
        self.pasos = pasos
        self.tiempo = tiempo
        self.largoA = len(cadA)
        self.largoB = len(cadB)
        self.hipA = hipA
        self.hipB = hipB

    def __str__(self):
        return "Cadena A:"+str(self.cadA)+", "+str(self.cadB)+", "+str(self.pasos) + ", " + str(self.tiempo)+", "+str(self.largoA)+", "+str(self.largoB)

    @staticmethod
    def pasos(arrayResultados):
        return np.array([x.pasos for x in arrayResultados])

    @staticmethod
    def tiempos(arrayResultados):
        return np.array([x.tiempo for x in arrayResultados])

    @staticmethod
    def hipotesisA(arrayResultados):
        return np.array([x.hipA for x in arrayResultados])

    @staticmethod
    def hipotesisB(arrayResultados):
        return np.array([x.hipB for x in arrayResultados])

    @staticmethod
    def errores(xx, yy):
        arr = []
        for i in range(len(xx)):
            arr.append(yy[i]-xx[i])
        return np.array(arr)
