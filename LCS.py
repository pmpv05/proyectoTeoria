def createMatrix(numero_filas, numero_columnas):
    matriz = [None] * numero_filas
    for i in range(numero_filas):
        matriz[i] = [-1] * numero_columnas
    return matriz

# Cálcula el largo de la LCS entre dos strings.
# Recursivo.
# INGENUO: TIEMPO EXPONENCIAL
# A = Primer string
# B = Segundo string
# a = Largo de la cadena - 1 del string A
# b = Largo de la cadena - 1 del string B


def RecursiveLCSLength(A, B, a, b):
    if a == 0 or b == 0:
        return 0
    elif A[a-1] == B[b-1]:
        return 1 + RecursiveLCSLength(A, B, a-1, b-1)
    return max(RecursiveLCSLength(A, B, a-1, b), RecursiveLCSLength(A, B, a, b-1))

# Cálcula la matriz de distancias a partir de 2 strings.
# Recursivo. Memoriza resultados intermedios.
# DINAMICO: TIEMPO POLINOMICO A*B
# A = Primer string
# B = Segundo string
# a = Largo de la cadena - 1 del string A
# b = Largo de la cadena - 1 del string B


def MemoryLCSLength(A, B, a, b, M):
    if M[a][b] is not None:
        return M[a][b]
    elif a == 0 or b == 0:
        result = 0
    elif A[a] == B[b]:
        result = 1 + MemoryLCSLength(A, B, a-1, b-1, M)
    else:
        result = max(MemoryLCSLength(A, B, a-1, b, M),
                     MemoryLCSLength(A, B, a, b-1, M))
    M[a][b] = result
    return result

# Cálcula la matriz de distancias a partir de 2 strings.
# Iterativo. Memoriza resultados previos.
# DINAMICO: TIEMPO POLINOMICO
# A = Primer string
# B = Segundo string

def IterativeLCSLength(A, B):
    len_A = len(A)
    len_B = len(B)
    M = createMatrix(len_A, len_B)

    for a in range(len_A):
        M[a][0] = 0
    for b in range(len_B):
        M[0][b] = 0
    for a in range(len_A):
        for b in range(len_B):
            if A[a] == B[b]:
                M[a][b] = M[a-1][b-1] + 1
            else:
                M[a][b] = max(M[a-1][b], M[a][b-1])
    return M[a][b]

# Obtiene la LCS a partir de la matriz de distancias.


def Backtrack(M, A, B, a, b):
    if a == 0 or b == 0:
        return ""
    elif A[a-1] == B[b-1]:
        return A[a-1] + Backtrack(M, A, B, a-1, b-1)
    elif M[a, b-1] > M[a-1, b]:
        return Backtrack(M, A, B, a, b-1)
    return Backtrack(M, A, B, a-1, b)
