import msvcrt as m

from Testing import Test
from Resultado import Resultado


def Menu():
    print("Ingrese el algoritmo a probar:", "1: Ingenuo",
          "2: Eficiente (default)", "3: Bottom-Up\n", sep="\n")

    opcionesAlg = {"1": Test.GenerateNaive,
                   "2": Test.GenerateEfficient, "3": Test.GenerateBottom}
    valueA = m.getwch()
    if valueA in opcionesAlg:
        a = opcionesAlg.get(valueA)
        print(valueA)
    else:
        a = opcionesAlg.get("2")
        print("2")

    print("Ingrese en número de repeticiones (default: 10)")
    try:
        n = int(input())
        print(n)
    except:
        n = 10
        print(n)

    print("Ingrese el  largo máximo para las listas (default: 10)")
    try:
        l = int(input())
        print(l)
    except:
        l = 10
        print(l)

    print("Ingrese la hipotesis a probar (A/B) (default: B):")
    opcionesHip = {"a": Resultado.HipotesisA, "b": Resultado.HipotesisB}
    valueH = m.getwch()
    if valueH in opcionesHip:
        h = opcionesHip.get(valueH)
        print(valueH)
    else:
        h = opcionesHip.get("b")
        print("b")

    return a, n, l, h


def Main():
    while True:
        a, n, l, h = Menu()
        print("\nEjecutando...\n")
        name = Test.GenerateRandomString(10)
        test = Test.GenerateTestSample(n, a, l)
        Test.TestHipotesis(test, h, True, name)
        Test.SaveToCSV(test, name)


Main()
