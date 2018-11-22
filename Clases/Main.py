import msvcrt as m

from Testing import Test
from Resultado import Resultado

def Menu():
	print("Ingrese el algoritmo a probar:","1: Ingenuo", "2: Eficiente (default)", "3: Bottom-Up\n", sep = "\n")
	a = {"1":Test.GenerateNaive, "2":Test.GenerateEfficient, "3":Test.GenerateBottom}.get(m.getwch(), "2")
	
	print("Ingrese en número de repeticiones (default: 10)")
	try:
		n = int(input())
	except:
		n = 10
	
	print("Ingrese el  largo máximo para las listas (default: 10)")
	try:
		l = int(input())
	except:
		l = 10

	print("Ingrese la hipotesis a probar (A/B) (default: A):")
	h = {"a":Resultado.HipotesisA, "b":Resultado.HipotesisB}.get(str.lower(m.getwch()), "a")

	return a, n, l, h

def Main():
	while True:
		a, n, l, h = Menu()
		name = Test.GenerateRandomString(10)
		test = Test.GenerateTestSample(n, a, l)
		Test.TestHipotesis(test, h, True, name)
		Test.SaveToCSV(test, name)

Main()