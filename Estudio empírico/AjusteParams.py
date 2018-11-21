import numpy as np
import matplotlib.pyplot as plt
from ResultadosPruebas import *

print("------- NAIVE HIPOTESIS 1 - PASOS EJECUTADOS -------")
hip1 = "2^(n*m)"
print("Se pretende llegar a una función y = mx + c, según el orden definido.")

# Cálculo de función de tiempo
A = np.vstack([naiveHip1, np.ones(len(naiveHip1))]).T
m, c = np.linalg.lstsq(A, naivePasosEj, rcond=None)[0]

funcionNaiveHip1Pasos = "y = " + str(m) + "x + " + str(c)
print("==> La función es: " + funcionNaiveHip1Pasos +
      " para HIPOTESIS 1 = " + hip1 + " y PASOS EJECUTADOS.")

# Gráfica
plt.plot(naiveHip1, naiveTiempos, 'o', label='Original data', markersize=10)
plt.plot(naiveHip1, m * naiveHip1 + c, 'r', label='Fitted line')
plt.legend()
plt.show()

##########################################################################################

print("------- NAIVE HIPOTESIS 1 - TIEMPOS -------")
hip1 = "2^(n*m)"
print("Se pretende llegar a una función y = mx + c, según el orden definido.")

# Cálculo de función de tiempo
A = np.vstack([naiveHip1, np.ones(len(naiveHip1))]).T
m, c = np.linalg.lstsq(A, naiveTiempos, rcond=None)[0]

funcionNaiveHip1Tiempos = "y = " + str(m) + "x + " + str(c)
print("==> La función es: " + funcionNaiveHip1Tiempos +
      " para HIPOTESIS 1 = " + hip1 + " y TIEMPOS.")

# Gráfica
plt.plot(naiveHip1, naiveTiempos, 'o', label='Original data', markersize=10)
plt.plot(naiveHip1, m * naiveHip1 + c, 'r', label='Fitted line')
plt.legend()
plt.show()

##########################################################################################
