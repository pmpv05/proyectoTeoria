# coding=utf-8

import random
import string
import time
from LCS import *
from LCS_Alg_Instrumentados import *


def stringGenerator(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

###################################################################################################


def testNaiveLCS(qtyTimes):
    print("Prueba Naive LCS (Recursivo): Mide tiempo")
    for i in range(qtyTimes):
        print("--> Ejecución " + str(i))
        strA = stringGenerator(random.randint(5, 20))
        strB = stringGenerator(random.randint(5, 20))
        largoStrA = len(strA)
        largoStrB = len(strB)
        print("Cadena A (largo = " + str(largoStrA) + "): " + strA)
        print("Cadena B (largo = " + str(largoStrB) + "): " + strB)

        # Tiempo
        start = time.perf_counter_ns()
        result = NaiveLCS(strA, strB,
                          largoStrA - 1, largoStrB - 1)
        timeResult = (time.perf_counter_ns() - start) / 1e9

        print("Tiempo real (segundos): " + str(timeResult))

        print("Resultado: " + str(result) + "\n")


def testNaiveLCS_DadosStrs(A, B, qtyTimes):
    print("Prueba Naive LCS (Recursivo) dadas las cadenas: Mide tiempo")
    for i in range(qtyTimes):
        print("--> Ejecución " + str(i))
        strA = A
        strB = B
        largoStrA = len(strA)
        largoStrB = len(strB)
        print("Cadena A (largo = " + str(largoStrA) + "): " + strA)
        print("Cadena B (largo = " + str(largoStrB) + "): " + strB)

        # Tiempo
        start = time.perf_counter_ns()
        result = NaiveLCS(strA, strB,
                          largoStrA - 1, largoStrB - 1)
        timeResult = (time.perf_counter_ns() - start) / 1e9

        print("Tiempo real (segundos): " + str(timeResult))

        print("Resultado: " + str(result) + "\n")


def testNaiveLCS_Inst(qtyTimes):
    print("Prueba Naive LCS (Recursivo) versión instrumentada: Mide pasos ejecutados y tiempo")
    for i in range(qtyTimes):
        print("--> Ejecución " + str(i))
        strA = stringGenerator(random.randint(5, 20))
        strB = stringGenerator(random.randint(5, 20))
        largoStrA = len(strA)
        largoStrB = len(strB)
        print("Cadena A (largo = " + str(largoStrA) + "): " + strA)
        print("Cadena B (largo = " + str(largoStrB) + "): " + strB)

        # Pasos ejecutados
        pasosEjecutados = []
        result = NaiveLCS_Inst(strA, strB,
                               largoStrA - 1, largoStrB - 1, pasosEjecutados)

        # Tiempo
        start = time.perf_counter_ns()
        result = NaiveLCS(strA, strB,
                          largoStrA - 1, largoStrB - 1)
        timeResult = (time.perf_counter_ns() - start) / 1e9

        print("Tiempo real (segundos): " + str(timeResult))

        print("Resultado: " + str(result) + "\n")


def testNaiveLCS_Inst_DadosStrs(A, B, qtyTimes):
    print("Prueba Naive LCS (Recursivo) versión instrumentada dadas las cadenas: Mide pasos ejecutados y tiempo")
    for i in range(qtyTimes):
        print("--> Ejecución "+str(i))
        strA = A
        strB = B
        largoStrA = len(strA)
        largoStrB = len(strB)
        print("Cadena A (largo = " + str(largoStrA) + "): " + strA)
        print("Cadena B (largo = " + str(largoStrB) + "): " + strB)

         # Pasos ejecutados
        pasosEjecutados = []
        result = NaiveLCS_Inst(strA, strB,
                               largoStrA - 1, largoStrB - 1, pasosEjecutados)

        # Tiempo
        start = time.perf_counter_ns()
        result = NaiveLCS(strA, strB,
                          largoStrA - 1, largoStrB - 1)
        timeResult = (time.perf_counter_ns() - start) / 1e9

        print("Tiempo real (segundos): " + str(timeResult))

        print("Resultado: " + str(result) + "\n")

###################################################################################################


def testEfficientLCS(qtyTimes):
    print("Prueba Efficient LCS (Prog. Din. Rec.): Mide tiempo")
    for i in range(qtyTimes):
        print("--> Ejecución "+str(i))
        strA = stringGenerator(random.randint(10, 50))
        strB = stringGenerator(random.randint(10, 50))
        largoStrA = len(strA)
        largoStrB = len(strB)
        print("Cadena A (largo = " + str(largoStrA) + "): " + strA)
        print("Cadena B (largo = " + str(largoStrB) + "): " + strB)

        matrix = Matrix(largoStrA, largoStrB)

        # Tiempo
        start = time.perf_counter_ns()
        result = EfficientLCS(strA, strB,
                              largoStrA - 1, largoStrB - 1, matrix)
        timeResult = (time.perf_counter_ns() - start) / 1e9

        print("Tiempo real (segundos): " + str(timeResult))

        print("Resultado: " + str(result) + "\n")


def testEfficientLCS_DadosStrs(A, B, qtyTimes):
    print("Prueba Efficient LCS (Prog. Din. Rec.) dadas las cadenas: Mide tiempo")
    for i in range(qtyTimes):
        print("--> Ejecución "+str(i))
        strA = A
        strB = B
        largoStrA = len(strA)
        largoStrB = len(strB)
        print("Cadena A (largo = " + str(largoStrA) + "): " + strA)
        print("Cadena B (largo = " + str(largoStrB) + "): " + strB)

        matrix = Matrix(largoStrA, largoStrB)

        # Tiempo
        start = time.perf_counter_ns()
        result = EfficientLCS(strA, strB,
                              largoStrA - 1, largoStrB - 1, matrix)
        timeResult = (time.perf_counter_ns() - start) / 1e9

        print("Tiempo real (segundos): " + str(timeResult))

        print("Resultado: " + str(result) + "\n")


def testEfficientLCS_Inst(qtyTimes):
    print("Prueba Efficient LCS (Prog. Din. Rec.): Mide accesos a la matriz y tiempo")
    for i in range(qtyTimes):
        print("--> Ejecución "+str(i))
        strA = stringGenerator(random.randint(10, 50))
        strB = stringGenerator(random.randint(10, 50))
        largoStrA = len(strA)
        largoStrB = len(strB)
        print("Cadena A (largo = " + str(largoStrA) + "): " + strA)
        print("Cadena B (largo = " + str(largoStrB) + "): " + strB)

        # Accesos a la matriz
        accesosMatriz = []
        matrix = Matrix(largoStrA, largoStrB)
        result = EfficientLCS_Inst(strA, strB,
                                   largoStrA - 1, largoStrB - 1, matrix, accesosMatriz)

        # Tiempo
        start = time.perf_counter_ns()
        result = EfficientLCS(strA, strB,
                              largoStrA - 1, largoStrB - 1, matrix)
        timeResult = (time.perf_counter_ns() - start) / 1e9

        print("Tiempo real (segundos): " + str(timeResult))

        print("Resultado: " + str(result) + "\n")


def testEfficientLCS_Inst_DadosStrs(A, B, qtyTimes):
    print("Prueba Efficient LCS (Prog. Din. Rec.) dadas las cadenas: Mide accesos a la matriz y tiempo")
    for i in range(qtyTimes):
        print("--> Ejecución "+str(i))
        strA = A
        strB = B
        largoStrA = len(strA)
        largoStrB = len(strB)
        print("Cadena A (largo = " + str(largoStrA) + "): " + strA)
        print("Cadena B (largo = " + str(largoStrB) + "): " + strB)

        # Accesos a la matriz
        accesosMatriz = []
        matrix = Matrix(largoStrA, largoStrB)
        result = EfficientLCS_Inst(strA, strB,
                                   largoStrA - 1, largoStrB - 1, matrix, accesosMatriz)

        # Tiempo
        start = time.perf_counter_ns()
        result = EfficientLCS(strA, strB,
                              largoStrA - 1, largoStrB - 1, matrix)
        timeResult = (time.perf_counter_ns() - start) / 1e9

        print("Tiempo real (segundos): " + str(timeResult))

        print("Resultado: " + str(result) + "\n")
###################################################################################################


def testBottomLCS(qtyTimes):
    print("Prueba Bottom LCS (Prog. Din. It.): Mide tiempo")
    for i in range(qtyTimes):
        print("--> Ejecución "+str(i))
        strA = stringGenerator(random.randint(10, 50))
        strB = stringGenerator(random.randint(10, 50))
        largoStrA = len(strA)
        largoStrB = len(strB)
        print("Cadena A (largo = " + str(largoStrA) + "): " + strA)
        print("Cadena B (largo = " + str(largoStrB) + "): " + strB)

        # Tiempo
        start = time.perf_counter_ns()
        result = BottomLCS(strA, strB)
        timeResult = (time.perf_counter_ns() - start) / 1e9

        print("Tiempo real (segundos): " + str(timeResult))

        print("Resultado: " + str(result) + "\n")


def testBottomLCS_DatosStrs(A, B, qtyTimes):
    print("Prueba Efficient LCS (Prog. Din. Rec.) dadas las cadenas: Mide tiempo")
    for i in range(qtyTimes):
        print("--> Ejecución "+str(i))
        strA = A
        strB = B
        largoStrA = len(strA)
        largoStrB = len(strB)
        print("Cadena A (largo = " + str(largoStrA) + "): " + strA)
        print("Cadena B (largo = " + str(largoStrB) + "): " + strB)

        # Tiempo
        start = time.perf_counter_ns()
        result = BottomLCS(strA, strB)
        timeResult = (time.perf_counter_ns() - start) / 1e9

        print("Tiempo real (segundos): " + str(timeResult))

        print("Resultado: " + str(result) + "\n")


def testBottomLCS_Inst(qtyTimes):
    print("Prueba Efficient LCS (Prog. Din. Rec.): Mide accesos a la matriz y tiempo")
    for i in range(qtyTimes):
        print("--> Ejecución "+str(i))
        strA = stringGenerator(random.randint(10, 50))
        strB = stringGenerator(random.randint(10, 50))
        largoStrA = len(strA)
        largoStrB = len(strB)
        print("Cadena A (largo = " + str(largoStrA) + "): " + strA)
        print("Cadena B (largo = " + str(largoStrB) + "): " + strB)

        # Accesos a la matriz
        accesosMatriz = 0
        result = BottomLCS_Inst(strA, strB, accesosMatriz)

        # Tiempo
        start = time.perf_counter_ns()
        result = BottomLCS(strA, strB)
        timeResult = (time.perf_counter_ns() - start) / 1e9

        print("Tiempo real (segundos): " + str(timeResult))

        print("Resultado: " + str(result) + "\n")


def testBottomLCS_Inst_DadosStrs(A, B, qtyTimes):
    print("Prueba Efficient LCS (Prog. Din. Rec.) dadas las cadenas: Mide accesos a la matriz y tiempo")
    for i in range(qtyTimes):
        print("--> Ejecución "+str(i))
        strA = A
        strB = B
        largoStrA = len(strA)
        largoStrB = len(strB)
        print("Cadena A (largo = " + str(largoStrA) + "): " + strA)
        print("Cadena B (largo = " + str(largoStrB) + "): " + strB)

        # Accesos a la matriz
        accesosMatriz = 0
        result = BottomLCS_Inst(strA, strB, accesosMatriz)

        # Tiempo
        start = time.perf_counter_ns()
        result = BottomLCS(strA, strB)
        timeResult = (time.perf_counter_ns() - start) / 1e9

        print("Tiempo real (segundos): " + str(timeResult))

        print("Resultado: " + str(result) + "\n")

###################################################################################################


"""" TEST NAIVE LCS """
print("----------------- TEST NAIVE LCS -----------------")
# testNaiveLCS(1)
# testNaiveLCS_DadosStrs("a", "a", 1)
testNaiveLCS_Inst(1)
# testNaiveLCS_Inst_DadosStrs("ccm", "uy", 1)

# """" TEST EFFICIENT LCS """
# print("----------------- TEST EFFICIENT LCS -----------------")
# testEfficientLCS(1)
# testEfficientLCS_DadosStrs("ba", "a", 1)
testEfficientLCS_Inst(1)
# testEfficientLCS_Inst_DadosStrs("bac", "afgg", 1)

# """" TEST BOTTOM LCS """
# print("----------------- TEST BOTTOM LCS -----------------")
# testBottomLCS(1)
# testBottomLCS_DatosStrs("a", "a", 1)
testBottomLCS_Inst(1)
# testBottomLCS_Inst_DadosStrs("bac", "afgg", 1)
