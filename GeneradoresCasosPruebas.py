# coding=utf-8

import random
import string
from LCS import *


def stringGenerator(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def testRecursiveLCSLength(qtyTimes):
    for i in range(qtyTimes):

        fstString = stringGenerator(random.randint(1, 20))
        sndString = stringGenerator(random.randint(1, 20))
        print(fstString)
        print(sndString)
        result = NaiveLCS(fstString, sndString,
                          len(fstString)-1, len(sndString)-1)
        print(result)


def testMemoryLCSLength(qtyTimes):
    for i in range(qtyTimes):

        fstString = stringGenerator(random.randint(1, 55))
        sndString = stringGenerator(random.randint(1, 55))
        print(fstString)
        print(sndString)
        matrix = Matrix(len(fstString), len(sndString))
        result = EfficientLCS(fstString, sndString,
                              len(fstString)-1, len(sndString)-1, matrix)
        print(result)


def testIterativeLCSLength(qtyTimes):
    for i in range(qtyTimes):
        fstString = stringGenerator(random.randint(1, 55))
        sndString = stringGenerator(random.randint(1, 55))
        print(fstString)
        print(sndString)
        result = BottomLCS(fstString, sndString)
        print(result)


testRecursiveLCSLength(1)
print("----")
testMemoryLCSLength(1)
print("----")
testIterativeLCSLength(1)
