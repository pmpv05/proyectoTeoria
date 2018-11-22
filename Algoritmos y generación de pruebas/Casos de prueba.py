import random
import string
import time
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

from Resultado import Resultado as R
from LCS_Instrumentados import *
from Resultado import *


def GenerateRandomString(length):
	letters = string.ascii_letters + string.digits
	return ''.join(random.choice(letters) for i in range(length))

def GenerateNaive(largoA, largoB):
	strA = GenerateRandomString(largoA)
	strB = GenerateRandomString(largoB)

	# Tiempo en ms y pasos ejecutados
	start = time.perf_counter_ns()
	pasosEjecutados = NaiveLCS_Inst(strA, strB, largoA, largoB)
	timeResult = (time.perf_counter_ns() - start) / 1e6

	return Resultado(strA, strB, pasosEjecutados, timeResult, pow((largoA*largoB), 2), pow(2, (largoA+largoB)))

def GenerateEfficient(largoA, largoB):
	strA = GenerateRandomString(largoA)
	strB = GenerateRandomString(largoB)

	# Tiempo en ms y pasos ejecutados
	start = time.perf_counter_ns()
	pasosEjecutados = EfficientLCS_Inst(strA, strB,largoA, largoB, Matrix(largoA+1, largoB+1))
	timeResult = (time.perf_counter_ns() - start) / 1e6

	return Resultado(strA, strB, pasosEjecutados, timeResult, pow(min(largoA, largoB), 2),largoA*largoB)

def GenerateBottom(largoA, largoB):
	strA = GenerateRandomString(largoA)
	strB = GenerateRandomString(largoB)

	# Tiempo en ms y pasos ejecutados
	start = time.perf_counter_ns()
	pasosEjecutados = BottomLCS_Inst(strA, strB)
	timeResult = (time.perf_counter_ns() - start) / 1e6

	return Resultado(strA, strB, pasosEjecutados, timeResult, pow((min(largoA, largoB), 2)), largoA*largoB)

def GenerateTestSample(n, LCS, maximo):
	arrResultados = []
	for i in range(n):
		arrResultados.append(LCS(random.randint(5, maximo), random.randint(5, maximo)))
	return arrResultados

def TestHipotesis(resultados, hip):
	hipA    = hip(resultados)
	pasos   = R.Pasos(resultados)
	tiempos = R.Tiempos(resultados)

	h_pasos = np.vstack([hipA, np.ones(len(hipA))]).T
	m_pasos, c_pasos = np.linalg.lstsq(h_pasos, pasos, rcond=None)[0]
	y_pasos = m_pasos * hipA + c_pasos

	h_tiempos = np.vstack([hipA, np.ones(len(hipA))]).T
	m_tiempos, c_tiempos = np.linalg.lstsq(h_tiempos, tiempos, rcond=None)[0]
	y_tiempos = m_tiempos * hipA + c_tiempos

	fig, axis = plt.subplots(2, 1, constrained_layout = True)
	axis[0].plot(hipA, pasos, 'go', label='Empírico')
	axis[0].plot(hipA, y_pasos, 'r-', label='Teórico')
	axis[0].set_title("Pasos")

	axis[1].plot(hipA, tiempos, 'go', label='Empírico')
	axis[1].plot(hipA, y_tiempos, 'r-', label='Teórico')
	axis[1].set_title("Tiempo")

	k2, p = stats.normaltest(R.Errores(pasos, y_pasos))
	alpha = 1e-3
	if p < alpha:  # null hypothesis: x comes from a normal distribution
		fig.suptitle("The null hypothesis can be rejected")
	else:
		fig.suptitle("The null hypothesis cannot be rejected")	
	plt.show()

TestHipotesis(GenerateTestSample(50, GenerateEfficient, 50), R.HipotesisA)
