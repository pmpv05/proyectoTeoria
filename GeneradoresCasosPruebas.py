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
    for i in range(qtyTimes):

        fstString = stringGenerator(random.randint(1, 20))
        sndString = stringGenerator(random.randint(1, 20))
        print(fstString)
        print(sndString)
        result = NaiveLCS(fstString, sndString,
                          len(fstString)-1, len(sndString)-1)
        print("Resultado: " + str(result))


def testNaiveLCS_DadosStrs(A, B, qtyTimes):
    for i in range(qtyTimes):

        fstString = A
        sndString = B
        print(fstString)
        print(sndString)
        result = NaiveLCS(fstString, sndString,
                          len(fstString)-1, len(sndString)-1)
        print("Resultado: " + str(result))


def testNaiveLCS_Inst(qtyTimes):
    for i in range(qtyTimes):

        fstString = stringGenerator(random.randint(1, 20))
        sndString = stringGenerator(random.randint(1, 20))
        print(fstString)
        print(sndString)
        pasosEjecutados = []
        result = NaiveLCS_Inst(fstString, sndString,
                               len(fstString)-1, len(sndString)-1, pasosEjecutados)
        print("Resultado: " + str(result))


def testNaiveLCS_Inst_DadosStrs(A, B, qtyTimes):
    for i in range(qtyTimes):

        fstString = A
        sndString = B
        print(fstString)
        print(sndString)
        pasosEjecutados = []
        result = NaiveLCS_Inst(fstString, sndString,
                               len(fstString)-1, len(sndString)-1, pasosEjecutados)
        print("Resultado: " + str(result))

###################################################################################################


def testEfficientLCS(qtyTimes):
    for i in range(qtyTimes):

        fstString = stringGenerator(random.randint(1, 55))
        sndString = stringGenerator(random.randint(1, 55))
        print(fstString)
        print(sndString)
        matrix = Matrix(len(fstString), len(sndString))
        result = EfficientLCS(fstString, sndString,
                              len(fstString)-1, len(sndString)-1, matrix)
        print("Resultado: " + str(result))


def testEfficientLCS_DadosStrs(A, B, qtyTimes):
    for i in range(qtyTimes):

        fstString = A
        sndString = B
        print(fstString)
        print(sndString)
        matrix = Matrix(len(fstString), len(sndString))
        result = EfficientLCS(fstString, sndString,
                              len(fstString)-1, len(sndString)-1, matrix)
        print("Resultado: " + str(result))


def testEfficientLCS_Inst(qtyTimes):
    for i in range(qtyTimes):

        fstString = stringGenerator(random.randint(1, 55))
        sndString = stringGenerator(random.randint(1, 55))
        print(fstString)
        print(sndString)
        accesosMatriz = []
        matrix = Matrix(len(fstString), len(sndString))
        result = EfficientLCS_Inst(fstString, sndString,
                                   len(fstString)-1, len(sndString)-1, matrix, accesosMatriz)
        print("Resultado: " + str(result))

def testEfficientLCS_Inst_DadosStrs(A,B, qtyTimes):
    for i in range(qtyTimes):

        fstString = A
        sndString = B
        print(fstString)
        print(sndString)
        accesosMatriz = []
        matrix = Matrix(len(fstString), len(sndString))
        result = EfficientLCS_Inst(fstString, sndString,
                                   len(fstString)-1, len(sndString)-1, matrix, accesosMatriz)
        print("Resultado: " + str(result))
###################################################################################################


def testBottomLCS(qtyTimes):
    for i in range(qtyTimes):
        fstString = stringGenerator(random.randint(1, 55))
        sndString = stringGenerator(random.randint(1, 55))
        print(fstString)
        print(sndString)
        result = BottomLCS(fstString, sndString)
        print("Resultado: " + str(result))


def testBottomLCS_DatosStrs(A, B, qtyTimes):
    for i in range(qtyTimes):
        fstString = A
        sndString = B
        print(fstString)
        print(sndString)
        result = BottomLCS(fstString, sndString)
        print("Resultado: " + str(result))


def testBottomLCS_Inst(qtyTimes):
    for i in range(qtyTimes):
        fstString = stringGenerator(random.randint(1, 55))
        sndString = stringGenerator(random.randint(1, 55))
        print(fstString)
        print(sndString)
        accesosMatriz = 0
        result = BottomLCS_Inst(fstString, sndString, accesosMatriz)
        print("Resultado: " + str(result))

def testBottomLCS_Inst_DadosStrs(A,B,qtyTimes):
    for i in range(qtyTimes):
        fstString = A
        sndString = B
        print(fstString)
        print(sndString)
        accesosMatriz = 0
        result = BottomLCS_Inst(fstString, sndString, accesosMatriz)
        print("Resultado: " + str(result))

###################################################################################################

"""" TEST NAIVE LCS """
print("----------------- TEST NAIVE LCS -----------------")
# testNaiveLCS(1)
# testNaiveLCS_DadosStrs("a", "a", 1)
# testNaiveLCS_Inst(1)
#testNaiveLCS_Inst_DadosStrs("ccm", "uy", 1)

"""" TEST EFFICIENT LCS """
print("----------------- TEST EFFICIENT LCS -----------------")
# testEfficientLCS(1)
# testEfficientLCS_DadosStrs("ba", "a", 1)
# testEfficientLCS_Inst(1)
testEfficientLCS_Inst_DadosStrs("bac", "afgg", 1)

"""" TEST BOTTOM LCS """
print("----------------- TEST BOTTOM LCS -----------------")
# testBottomLCS(1)
# testBottomLCS_DatosStrs("a", "a", 1)
# testBottomLCS_Inst(1)
testBottomLCS_Inst_DadosStrs("bac", "afgg", 1)
