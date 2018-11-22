import random
import string
import time
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

from LCS_Instrumentados import *
from Resultado import *


def stringGenerator(length):
    """
    Devuelve una cadena aleatoria de letras minúsculas.
        length = Largo que debe tener la cadena
    """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def testNaiveLCSUnCaso(largoA, largoB):
    """
    Ejecuta el algoritmo NAIVE (INGENUO: TIEMPO EXPONENCIAL) y devuelve un objeto Resultado con todos los datos de la ejecución.
        largoA = Largo que debe tener la primera cadena
        largoB = Largo que debe tener la segunda cadena
    """
    strA = stringGenerator(largoA)
    strB = stringGenerator(largoB)

    # Tiempo en ms y pasos ejecutados
    start = time.perf_counter_ns()
    pasosEjecutados = NaiveLCS_Inst(strA, strB,
                                    largoA-1, largoB-1)
    timeResult = (time.perf_counter_ns() - start) / 1e6

    return Resultado(strA, strB, pasosEjecutados, timeResult, pow((largoA*largoB), 2), pow(2, (largoA+largoB)))


def testEfficientLCSUnCaso(largoA, largoB):
    """
    Ejecuta el algoritmo EFFICIENT (DINAMICO) y devuelve un objeto Resultado con todos los datos de la ejecución.
        largoA = Largo que debe tener la primera cadena
        largoB = Largo que debe tener la segunda cadena
    """
    strA = stringGenerator(largoA)
    strB = stringGenerator(largoB)

    # Tiempo en ms y pasos ejecutados
    start = time.perf_counter_ns()
    pasosEjecutados = EfficientLCS_Inst(strA, strB,
                                        largoA-1, largoB-1, Matrix(largoA, largoB))
    timeResult = (time.perf_counter_ns() - start) / 1e6

    return Resultado(strA, strB, pasosEjecutados, timeResult, pow((min(largoA, largoB), 2)), largoA*largoB)


def testBottomLCSUnCaso(largoA, largoB):
    """
    Ejecuta el algoritmo BOTTOM (DINAMICO) y devuelve un objeto Resultado con todos los datos de la ejecución.
        largoA = Largo que debe tener la primera cadena
        largoB = Largo que debe tener la segunda cadena
    """
    strA = stringGenerator(largoA)
    strB = stringGenerator(largoB)

    # Tiempo en ms y pasos ejecutados
    start = time.perf_counter_ns()
    pasosEjecutados = BottomLCS_Inst(strA, strB)
    timeResult = (time.perf_counter_ns() - start) / 1e6

    return Resultado(strA, strB, pasosEjecutados, timeResult, pow((min(largoA, largoB), 2)), largoA*largoB)


def testNCasos(qtyTimes, algoritmo, maximo):
    """
    Ejecuta el algoritmo pasado como parámetro (algoritmo) qtyTimes veces y devuelve un 
        qtyTimes = Cantidad de veces a ejecutar el algoritmo
        algoritmo = Largo que debe tener la segunda cadena
        maximo
    """
    arrResultados = []
    for i in range(qtyTimes):
        arrResultados.append(
            algoritmo(random.randint(5, maximo), random.randint(5, maximo)))
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
