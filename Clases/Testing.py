import random
import string
import os
import time
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

from LCS import LCS
from Resultado import Resultado

class Test:
	@staticmethod
	def GenerateRandomString(length, rand = False):
		letters = string.ascii_letters + string.digits
		if rand:
			length = random.randint(2, length)
		return ''.join(random.choice(letters) for i in range(length)), length

	@staticmethod
	def GenerateNaive(lengthA, lengthB):
		strA, lengthA = Test.GenerateRandomString(lengthA)
		strB, lengthB = Test.GenerateRandomString(lengthB)

		# Tiempo en ms y pasos ejecutados
		start = time.perf_counter_ns()
		pasos = LCS.NaiveLCS_Inst(strA, strB, lengthA, lengthB)
		tiempo = (time.perf_counter_ns() - start) / 1e6
		return Resultado(strA, strB, pasos, tiempo, (lengthA*lengthB)**2, 2**(lengthA+lengthB))

	@staticmethod
	def GenerateEfficient(lengthA, lengthB):
		strA, lengthA = Test.GenerateRandomString(lengthA)
		strB, lengthB = Test.GenerateRandomString(lengthB)

		# Tiempo en ms y pasos ejecutados
		start = time.perf_counter_ns()
		pasos = LCS.EfficientLCS_Inst(strA, strB,lengthA, lengthB, LCS.Matrix(lengthA+1, lengthB+1))
		tiempo = (time.perf_counter_ns() - start) / 1e6
		return Resultado(strA, strB, pasos, tiempo, min(lengthA, lengthB)**2, lengthA*lengthB)

	@staticmethod
	def GenerateBottom(lengthA, lengthB):
		strA, lengthA = Test.GenerateRandomString(lengthA)
		strB, lengthB = Test.GenerateRandomString(lengthB)

		# Tiempo en ms y pasos ejecutados
		start = time.perf_counter_ns()
		pasos = LCS.BottomLCS_Inst(strA, strB)
		tiempo = (time.perf_counter_ns() - start) / 1e6
		return Resultado(strA, strB, pasos, tiempo, min(lengthA, lengthB)**2, lengthA*lengthB)

	@staticmethod
	def GenerateTestSample(n, lcs, maximo, minimo = 1):
		arrResultados = []
		for _ in range(n):
			arrResultados.append(lcs(random.randint(minimo, maximo), random.randint(minimo, maximo)))
			print(_)
		return arrResultados

	@staticmethod
	def TestHipotesis(results, hip, save = False, name = "", show = True):
		hipA    = hip(results)
		pasos   = Resultado.Pasos(results)
		tiempos = Resultado.Tiempos(results)

		h_pasos = np.vstack([hipA, np.ones(len(hipA))]).T
		m_pasos, c_pasos = np.linalg.lstsq(h_pasos, pasos, rcond=None)[0]
		y_pasos = m_pasos * hipA + c_pasos

		h_tiempos = np.vstack([hipA, np.ones(len(hipA))]).T
		m_tiempos, c_tiempos = np.linalg.lstsq(h_tiempos, tiempos, rcond=None)[0]
		y_tiempos = m_tiempos * hipA + c_tiempos

		errores = Resultado.Errores(pasos, y_pasos)
		Resultado.SetErrores(results, errores)
		_, p = stats.normaltest(errores)
		alpha = 0.001

		fig, axis = plt.subplots(3, 1, constrained_layout = True)
		axis[0].plot(hipA, pasos, 'go', label='Empírico', markersize = 3)
		axis[0].plot(hipA, y_pasos, 'r-', label='Teórico')
		axis[0].set_title("Pasos")

		axis[1].plot(hipA, tiempos, 'go', label='Empírico', markersize = 3)
		axis[1].plot(hipA, y_tiempos, 'r-', label='Teórico')
		axis[1].set_title("Tiempo")

		axis[2].hist(errores, bins = 100)
		axis[2].set_title("Errores")

		# while p < alpha:
		# 	alpha -= 0.0001
		print("p: " + str(p), "alpha: " + str(alpha))
		# fig.suptitle("La hipotesis no puede ser rechazada")	
		# if p < alpha:
		# 	fig.suptitle("La hipotesis puede ser rechazada")
		# else:
		# 	fig.suptitle("La hipotesis no puede ser rechazada")	

		if save:
			current_path = os.getcwd() + "\\Resultados"
			if not os.path.exists(current_path):
				os.makedirs(current_path)
			fig.savefig(current_path + "/" + name + ".png")

		if show:
			plt.show()

	@staticmethod
	def TestAll(n = 10000, l = 100):
		prueba = Test.GenerateTestSample(n, Test.GenerateEfficient, l)
		Test.TestHipotesis(prueba, Resultado.HipotesisA, True, "EFFICIENT - HIP A", False)
		Test.SaveToCSV(prueba, "EFFICIENT - HIP A")
		Test.TestHipotesis(prueba, Resultado.HipotesisB, True, "EFFICIENT - HIP B", False)
		Test.SaveToCSV(prueba, "EFFICIENT - HIP B")

		prueba = Test.GenerateTestSample(n, Test.GenerateBottom, l)
		Test.TestHipotesis(prueba, Resultado.HipotesisA, True, "BOTTOM-UP - HIP A", False)
		Test.SaveToCSV(prueba, "BOTTOM-UP - HIP A")
		Test.TestHipotesis(prueba, Resultado.HipotesisB, True, "BOTTOM-UP - HIP B", False)
		Test.SaveToCSV(prueba, "BOTTOM-UP - HIP B")

		# prueba = Test.GenerateTestSample(n, Test.GenerateNaive, l)
		# Test.TestHipotesis(prueba, Resultado.HipotesisA, True, "NAIVE - HIP A", False)
		# Test.SaveToCSV(prueba, "NAIVE - HIP A")
		# Test.TestHipotesis(prueba, Resultado.HipotesisB, True, "NAIVE - HIP B", False)
		# Test.SaveToCSV(prueba, "NAIVE - HIP B")

	@staticmethod
	def SaveToCSV(results, name):
		current_path = os.getcwd() + "\\Resultados"
		if not os.path.exists(current_path):
			os.makedirs(current_path)
		with open(current_path + "/" + str(name) + ".csv", "w") as csv:
			csv.write("Cadena A,Largo A,Cadena B,Largo B,Pasos,Tiempo(ms),Hipotesis A,HipotesisB,Error\n")
			for result in results:
				csv.write(str(result) + "\n")

Test.TestAll(10000, 100)