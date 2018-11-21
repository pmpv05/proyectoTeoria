# coding=utf-8


def Matrix(numero_filas, numero_columnas):
    return [[None]*numero_columnas for i in range(numero_filas)]


def NaiveLCS_Inst(A, B, a, b, lstPasos):
    """
    Cálcula el largo de la LCS entre dos strings.
    Recursivo.
    INGENUO: TIEMPO EXPONENCIAL
        A = Primer string
        B = Segundo string
        a = Largo de la cadena - 1 del string A
        b = Largo de la cadena - 1 del string B
    """

    if a == -1 or b == -1:
        lstPasos.append(1)
        result = 0
    elif A[a] == B[b]:
        lstPasos.append(1)
        result = 1 + NaiveLCS_Inst(A, B, a-1, b-1, lstPasos)
    else:
        lstPasos.append(1)
        result = max(NaiveLCS_Inst(A, B, a-1, b, lstPasos),
                     NaiveLCS_Inst(A, B, a, b-1, lstPasos))

    if(a == len(A)-1 and b == len(B)-1):
        print("Pasos ejecutados: " + str(sum(lstPasos)))
    return result


def EfficientLCS_Inst(A, B, a, b, M, lstAccesosMatriz):
    """
    Cálcula la matriz de distancias a partir de 2 strings.
    Recursivo. Memoriza resultados intermedios.
    DINAMICO: TIEMPO POLINOMICO A*B
        A = Primer string
        B = Segundo string
        a = Largo de la cadena - 1 del string A
        b = Largo de la cadena - 1 del string B
    """
    if a == -1 or b == -1:
        result = 0
    elif M[a][b] is not None:
        lstAccesosMatriz.append(1)
        return M[a][b]
    elif A[a] == B[b]:
        lstAccesosMatriz.append(1)
        result = 1 + EfficientLCS_Inst(A, B, a-1, b-1, M, lstAccesosMatriz)
    else:
        lstAccesosMatriz.append(1)
        result = max(EfficientLCS_Inst(A, B, a-1, b, M, lstAccesosMatriz),
                     EfficientLCS_Inst(A, B, a, b-1, M, lstAccesosMatriz))
    if a > -1 and b > -1:
        lstAccesosMatriz.append(1)
        M[a][b] = result

    if(a == len(A)-1 and b == len(B)-1):
        print("Accesos a matriz: " + str(sum(lstAccesosMatriz)))
    return result


def BottomLCS_Inst(A, B, accesosMatriz):
    """
    Cálcula la matriz de distancias a partir de 2 strings.
    Iterativo. Memoriza resultados previos.
    DINAMICO: TIEMPO POLINOMICO
        A = Primer string
        B = Segundo string
    """
    len_A = len(A)
    len_B = len(B)
    M = Matrix(len_A+1, len_B+1)

    for a in range(len_A+1):
        for b in range(len_B+1):
            if a == 0 or b == 0:
                accesosMatriz += 1
                M[a][b] = 0
            elif A[a-1] == B[b-1]:
                accesosMatriz += 1
                M[a][b] = M[a-1][b-1] + 1
            else:
                accesosMatriz += 1
                M[a][b] = max(M[a-1][b], M[a][b-1])

    print("Accesos a matriz: " + str(accesosMatriz))
    return M[a][b]


def Backtrack(M, A, B, a, b):
    """
    Obtiene la LCS a partir de la matriz de distancias.
    """
    if a == 0 or b == 0:
        return ""
    elif A[a-1] == B[b-1]:
        return A[a-1] + Backtrack(M, A, B, a-1, b-1)
    elif M[a, b-1] > M[a-1, b]:
        return Backtrack(M, A, B, a, b-1)
    return Backtrack(M, A, B, a-1, b)
