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
        result = RecursiveLCSLength(fstString, sndString,
                                    len(fstString)-1, len(sndString)-1)
        print(result)


def testMemoryLCSLength(qtyTimes):

    for i in range(qtyTimes):

        fstString = stringGenerator(random.randint(1, 55))
        sndString = stringGenerator(random.randint(1, 55))
        print(fstString)
        print(sndString)
        matrix = createMatrix(len(fstString), len(sndString))
        result = MemoryLCSLength(fstString, sndString,
                                 len(fstString)-1, len(sndString)-1, matrix)
        print(matrix)
        print(result)


def testIterativeLCSLength(qtyTimes):
    for i in range(qtyTimes):
        fstString = stringGenerator(random.randint(1, 55))
        sndString = stringGenerator(random.randint(1, 55))
        print(fstString)
        print(sndString)
        result = IterativeLCSLength(fstString, sndString)
        print(result)


# print([[0 for x in range(2)] for y in range(2)])
#createMatrix(2, 8)
testIterativeLCSLength(1)
# createMatrix2(6, 2)
