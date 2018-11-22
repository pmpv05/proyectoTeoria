# coding=utf-8


def Matrix(numero_filas, numero_columnas):
    return [[None]*numero_columnas for i in range(numero_filas)]


def NaiveLCS_Inst(A, B, a, b):
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
        return 1
    elif A[a] == B[b]:
        return 1 + NaiveLCS_Inst(A, B, a-1, b-1)
    else:
        return 1 + NaiveLCS_Inst(A, B, a-1, b) + NaiveLCS_Inst(A, B, a, b-1)


def EfficientLCS_Inst(A, B, a, b, M):
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
        return 1
    if M[a][b] is not None:
        return 0
    elif A[a] == B[b]:
        result = 1 + EfficientLCS_Inst(A, B, a-1, b-1, M)
    else:
        result = 1 + EfficientLCS_Inst(A, B, a-1, b, M) + \
            EfficientLCS_Inst(A, B, a, b-1, M)

    if a > -1 and b > -1:
        M[a][b] = result

    return result


str1 = 'dabs'
str2 = 'dfdsf'
print(EfficientLCS_Inst(str1, str2, len(str1)-1,
                        len(str2)-1, Matrix(len(str1), len(str2))))


def BottomLCS_Inst(A, B):
    """
    Cálcula la matriz de distancias a partir de 2 strings.
    Iterativo. Memoriza resultados previos.
    DINAMICO: TIEMPO POLINOMICO
        A = Primer string
        B = Segundo string
    """
    accesosMatriz = 0
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

    return accesosMatriz
