# coding=utf-8


def Matrix(numero_filas, numero_columnas):
    return [[None]*numero_columnas for i in range(numero_filas)]


def NaiveLCS(A, B, a, b):
    """
    Cálcula el largo de la LCS entre dos strings.
    Recursivo.
    INGENUO: TIEMPO EXPONENCIAL
        A = Primer string
        B = Segundo string
        a = Largo de la cadena - 1 del string A
        b = Largo de la cadena - 1 del string B
    """
    if a == 0 or b == 0:
        return 0
    elif A[a-1] == B[b-1]:
        return 1 + NaiveLCS(A, B, a-1, b-1)
    return max(NaiveLCS(A, B, a-1, b), NaiveLCS(A, B, a, b-1))


def EfficientLCS(A, B, a, b, M):
    """
    Cálcula la matriz de distancias a partir de 2 strings.
    Recursivo. Memoriza resultados intermedios.
    DINAMICO: TIEMPO POLINOMICO A*B
        A = Primer string
        B = Segundo string
        a = Largo de la cadena - 1 del string A
        b = Largo de la cadena - 1 del string B
    """
    if M[a][b] is not None:
        return M[a][b]
    elif a == 0 or b == 0:
        result = 0
    elif A[a] == B[b]:
        result = 1 + EfficientLCS(A, B, a-1, b-1, M)
    else:
        result = max(EfficientLCS(A, B, a-1, b, M),
                     EfficientLCS(A, B, a, b-1, M))
    M[a][b] = result
    return result


def BottomLCS(A, B):
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
                M[a][b] = 0
            elif A[a-1] == B[b-1]:
                M[a][b] = M[a-1][b-1] + 1
            else:
                M[a][b] = max(M[a-1][b], M[a][b-1])
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
