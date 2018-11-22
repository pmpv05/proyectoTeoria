import random
import string
import time
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from LCS_Instrumentados import *


def stringGenerator(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


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


def testNaiveLCSUnCaso(largoA, largoB):
    strA = stringGenerator(largoA)
    strB = stringGenerator(largoB)

    # Tiempo en ms y pasos ejecutados
    start = time.perf_counter_ns()
    pasosEjecutados = NaiveLCS_Inst(strA, strB,
                                    largoA, largoB)
    timeResult = (time.perf_counter_ns() - start) / 1e6

    return Resultado(strA, strB, pasosEjecutados, timeResult, pow((largoA*largoB), 2), pow(2, (largoA+largoB)))


def testEfficientLCSUnCaso(largoA, largoB):
    strA = stringGenerator(largoA)
    strB = stringGenerator(largoB)

    # Tiempo en ms y pasos ejecutados
    start = time.perf_counter_ns()
    pasosEjecutados = EfficientLCS_Inst(strA, strB,
                                        largoA, largoB, Matrix(largoA, largoB))
    timeResult = (time.perf_counter_ns() - start) / 1e6

    return Resultado(strA, strB, pasosEjecutados, timeResult, pow((min(largoA, largoB), 2)), largoA*largoB)


def testBottomLCSUnCaso(largoA, largoB):
    strA = stringGenerator(largoA)
    strB = stringGenerator(largoB)

    # Tiempo en ms y pasos ejecutados
    start = time.perf_counter_ns()
    pasosEjecutados = BottomLCS_Inst(strA, strB)
    timeResult = (time.perf_counter_ns() - start) / 1e6

    return Resultado(strA, strB, pasosEjecutados, timeResult, pow((min(largoA, largoB), 2)), largoA*largoB)


def testNCasos(qtyTimes, fun, maximo):
    arrResultados = []
    for i in range(qtyTimes):
        arrResultados.append(
            fun(random.randint(5, maximo), random.randint(5, maximo)))
    return arrResultados


a = testNCasos(50, testNaiveLCSUnCaso, 10)
for i in range(len(a)):
    print(a[i])

arrHipA = Resultado.hipotesisA(a)
arrHipB = Resultado.hipotesisB(a)
tiempos = Resultado.tiempos(a)
pasos = Resultado.pasos(a)

print("------- NAIVE HIPOTESIS 1 - PASOS EJECUTADOS -------")
hip1 = "(m*n)^2"
print("Se pretende llegar a una función y = mx + c, según el orden definido.")

# Cálculo de función de tiempo
A = np.vstack([arrHipB, np.ones(len(arrHipB))]).T
m, c = np.linalg.lstsq(A, pasos, rcond=None)[0]

funcionNaiveHip1Pasos = "y = " + str(m) + "x + " + str(c)
print("==> La función es: " + funcionNaiveHip1Pasos +
      " para HIPOTESIS 1 = " + hip1 + " y PASOS EJECUTADOS.")

y = m * arrHipB + c
# Gráfica
# plt.plot(arrHipA, pasos, 'o', label='Original data', markersize=10)
# plt.plot(arrHipA, y, 'r', label='Fitted line')
# plt.legend()
# plt.show()

print(y[5])
print(pasos[5])
print(Resultado.errores(pasos, y)[5])

k2, p = stats.normaltest(Resultado.errores(pasos, y))
alpha = 1e-3
print("p = {:g}".format(p))
p = 3.27207e-11
if p < alpha:  # null hypothesis: x comes from a normal distribution
    print("The null hypothesis can be rejected")
else:
    print("The null hypothesis cannot be rejected")
