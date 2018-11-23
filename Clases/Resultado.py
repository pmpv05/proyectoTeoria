import numpy as np
import math

class Resultado:
	def __init__(self, cadA, cadB, pasos, tiempo, hipA, hipB):
		self.cadA = cadA
		self.cadB = cadB
		self.pasos = pasos
		self.tiempo = tiempo
		self.largoA = len(cadA)
		self.largoB = len(cadB)
		self.hipA = math.ceil(hipA)
		self.hipB = math.ceil(hipB)
		self.y_pasos = None
		self.y_tiempo = None
		self.error_pasos = None
		self.error_tiempo = None

	def __str__(self):
		return "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11}".format(self.cadA, self.largoA, self.cadB, self.largoB, self.pasos, self.tiempo, self.hipA, self.hipB, self.y_pasos, self.error_pasos, self.y_tiempo, self.error_tiempo)

	@staticmethod
	def Pasos(results):
		return np.array([x.pasos for x in results])

	@staticmethod
	def Tiempos(results):
		return np.array([x.tiempo for x in results])

	@staticmethod
	def HipotesisA(results):
		return np.array([x.hipA for x in results])

	@staticmethod
	def HipotesisB(results):
		return np.array([x.hipB for x in results])

	@staticmethod
	def Errores(x, y):
		arr = []
		for i in range(len(x)):
			arr.append(x[i]-y[i])
		return np.array(arr)

	@staticmethod
	def SetErroresPasos(x, errores):
		for i in range(len(x)):
			x[i].error_pasos = errores[i]

	@staticmethod
	def SetErroresTiempo(x, errores):
		for i in range(len(x)):
			x[i].error_tiempo = errores[i]

	@staticmethod
	def SetYPasos(x, y):
		for i in range(len(x)):
			x[i].y_pasos = y[i]

	@staticmethod
	def SetYTiempo(x, y):
		for i in range(len(x)):
			x[i].y_tiempo = y[i]