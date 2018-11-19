# coding=utf-8

import random
import string
from LCS import *
from LCS_Alg_Instrumentados import *


def stringGenerator(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

###################################################################################################


def testNaiveLCS(qtyTimes):
        print("testNaiveLCS")
        for i in range(qtyTimes):
                print("--> Ejecución "+str(i))
                strA = stringGenerator(random.randint(1, 20))
                strB = stringGenerator(random.randint(1, 20))
                largoStrA = len(strA)
                largoStrB = len(strB)
                print("Cadena A (largo = " + str(largoStrA) + "): " + strA)
                print("Cadena B (largo = " + str(largoStrB) + "): " + strB)

                result = NaiveLCS(strA, strB,
                                largoStrA - 1, largoStrB - 1)
                print("Resultado: " + str(result) + "\n")


def testNaiveLCS_DadosStrs(A, B, qtyTimes):
        print("testNaiveLCS_DadosStrs")
        for i in range(qtyTimes):
                print("--> Ejecución "+str(i))
                strA = A
                strB = B
                largoStrA = len(strA)
                largoStrB = len(strB)
                print("Cadena A (largo = " + str(largoStrA) + "): " + strA)
                print("Cadena B (largo = " + str(largoStrB) + "): " + strB)

                result = NaiveLCS(strA, strB,
                                largoStrA - 1, largoStrB - 1)

                print("Resultado: " + str(result) + "\n")


def testNaiveLCS_Inst(qtyTimes):
        print("testNaiveLCS_Inst")
        for i in range(qtyTimes):
                print("--> Ejecución "+str(i))
                strA = stringGenerator(random.randint(1, 20))
                strB = stringGenerator(random.randint(1, 20))
                largoStrA = len(strA)
                largoStrB = len(strB)
                print("Cadena A (largo = " + str(largoStrA) + "): " + strA)
                print("Cadena B (largo = " + str(largoStrB) + "): " + strB)

                pasosEjecutados = []
                result = NaiveLCS_Inst(strA, strB,
                                largoStrA - 1, largoStrB - 1, pasosEjecutados)

                print("Resultado: " + str(result) + "\n")


def testNaiveLCS_Inst_DadosStrs(A, B, qtyTimes):
        print("testNaiveLCS_Inst_DadosStrs")
        for i in range(qtyTimes):
                print("--> Ejecución "+str(i))
                strA = A
                strB = B
                largoStrA = len(strA)
                largoStrB = len(strB)
                print("Cadena A (largo = " + str(largoStrA) + "): " + strA)
                print("Cadena B (largo = " + str(largoStrB) + "): " + strB)

                pasosEjecutados = []
                result = NaiveLCS_Inst(strA, strB,
                                largoStrA - 1, largoStrB - 1, pasosEjecutados)

                print("Resultado: " + str(result) + "\n")

###################################################################################################


def testEfficientLCS(qtyTimes):
        print("testEfficientLCS")
        for i in range(qtyTimes):
                print("--> Ejecución "+str(i))
                strA = stringGenerator(random.randint(1, 20))
                strB = stringGenerator(random.randint(1, 20))
                largoStrA = len(strA)
                largoStrB = len(strB)
                print("Cadena A (largo = " + str(largoStrA) + "): " + strA)
                print("Cadena B (largo = " + str(largoStrB) + "): " + strB)

                matrix = Matrix(largoStrA, largoStrB)
                result = EfficientLCS(strA, strB,
                                largoStrA - 1, largoStrB - 1, matrix)

                print("Resultado: " + str(result) + "\n")


def testEfficientLCS_DadosStrs(A, B, qtyTimes):
        print("testEfficientLCS_DadosStrs")
        for i in range(qtyTimes):
                print("--> Ejecución "+str(i))
                strA = A
                strB = B
                largoStrA = len(strA)
                largoStrB = len(strB)
                print("Cadena A (largo = " + str(largoStrA) + "): " + strA)
                print("Cadena B (largo = " + str(largoStrB) + "): " + strB)

                matrix = Matrix(largoStrA, largoStrB)
                result = EfficientLCS(strA, strB,
                                largoStrA - 1, largoStrB - 1, matrix)

                print("Resultado: " + str(result) + "\n")


def testEfficientLCS_Inst(qtyTimes):
        print("testEfficientLCS_Inst")
        for i in range(qtyTimes):
                print("--> Ejecución "+str(i))
                strA = stringGenerator(random.randint(1, 20))
                strB = stringGenerator(random.randint(1, 20))
                largoStrA = len(strA)
                largoStrB = len(strB)
                print("Cadena A (largo = " + str(largoStrA) + "): " + strA)
                print("Cadena B (largo = " + str(largoStrB) + "): " + strB)

                accesosMatriz = []
                matrix = Matrix(largoStrA, largoStrB)
                result = EfficientLCS_Inst(strA, strB,
                                largoStrA - 1, largoStrB - 1, matrix, accesosMatriz)

                print("Resultado: " + str(result) + "\n")


def testEfficientLCS_Inst_DadosStrs(A, B, qtyTimes):
        print("testEfficientLCS_Inst_DadosStrs")
        for i in range(qtyTimes):
                print("--> Ejecución "+str(i))
                strA = A
                strB = B
                largoStrA = len(strA)
                largoStrB = len(strB)
                print("Cadena A (largo = " + str(largoStrA) + "): " + strA)
                print("Cadena B (largo = " + str(largoStrB) + "): " + strB) 

                accesosMatriz = []
                matrix = Matrix(largoStrA, largoStrB)
                result = EfficientLCS_Inst(strA, strB,
                                largoStrA - 1, largoStrB - 1, matrix, accesosMatriz)

                print("Resultado: " + str(result) + "\n")
###################################################################################################


def testBottomLCS(qtyTimes):
        print("testBottomLCS")
        for i in range(qtyTimes):
                print("--> Ejecución "+str(i))
                strA = stringGenerator(random.randint(1, 20))
                strB = stringGenerator(random.randint(1, 20))
                largoStrA = len(strA)
                largoStrB = len(strB)
                print("Cadena A (largo = " + str(largoStrA) + "): " + strA)
                print("Cadena B (largo = " + str(largoStrB) + "): " + strB) 

                result = BottomLCS(strA, strB)

                print("Resultado: " + str(result) + "\n")


def testBottomLCS_DatosStrs(A, B, qtyTimes):
        print("testBottomLCS_DatosStrs")
        for i in range(qtyTimes):
                print("--> Ejecución "+str(i))
                strA = A
                strB = B
                largoStrA = len(strA)
                largoStrB = len(strB)
                print("Cadena A (largo = " + str(largoStrA) + "): " + strA)
                print("Cadena B (largo = " + str(largoStrB) + "): " + strB) 

                result = BottomLCS(strA, strB)

                print("Resultado: " + str(result) + "\n")


def testBottomLCS_Inst(qtyTimes):
        print("testBottomLCS_Inst")
        for i in range(qtyTimes):
                print("--> Ejecución "+str(i))
                strA = stringGenerator(random.randint(1, 20))
                strB = stringGenerator(random.randint(1, 20))
                largoStrA = len(strA)
                largoStrB = len(strB)
                print("Cadena A (largo = " + str(largoStrA) + "): " + strA)
                print("Cadena B (largo = " + str(largoStrB) + "): " + strB) 

                accesosMatriz = 0
                result = BottomLCS_Inst(strA, strB, accesosMatriz)

                print("Resultado: " + str(result) + "\n")

def testBottomLCS_Inst_DadosStrs(A, B, qtyTimes):
        print("testBottomLCS_Inst_DadosStrs")
        for i in range(qtyTimes):
                print("--> Ejecución "+str(i))
                strA = A
                strB = B
                largoStrA = len(strA)
                largoStrB = len(strB)
                print("Cadena A (largo = " + str(largoStrA) + "): " + strA)
                print("Cadena B (largo = " + str(largoStrB) + "): " + strB) 

                accesosMatriz = 0
                result = BottomLCS_Inst(strA, strB, accesosMatriz)

                print("Resultado: " + str(result) + "\n")

###################################################################################################

"""" TEST NAIVE LCS """
print("----------------- TEST NAIVE LCS -----------------")
testNaiveLCS(1)
testNaiveLCS_DadosStrs("a", "a", 1)
testNaiveLCS_Inst(1)
testNaiveLCS_Inst_DadosStrs("ccm", "uy", 1)

"""" TEST EFFICIENT LCS """
print("----------------- TEST EFFICIENT LCS -----------------")
testEfficientLCS(1)
testEfficientLCS_DadosStrs("ba", "a", 1)
testEfficientLCS_Inst(1)
testEfficientLCS_Inst_DadosStrs("bac", "afgg", 1)

"""" TEST BOTTOM LCS """
print("----------------- TEST BOTTOM LCS -----------------")
testBottomLCS(1)
testBottomLCS_DatosStrs("a", "a", 1)
testBottomLCS_Inst(1)
testBottomLCS_Inst_DadosStrs("bac", "afgg", 1)
