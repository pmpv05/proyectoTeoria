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
		a = Largo de la cadena del string A
		b = Largo de la cadena del string B
	"""
	if a == 0 or b == 0:
		return 1
	elif A[a-1] == B[b-1]:
		return 1 + NaiveLCS_Inst(A, B, a-1, b-1)
	return 1 + NaiveLCS_Inst(A, B, a-1, b) + NaiveLCS_Inst(A, B, a, b-1)

def EfficientLCS_Inst(A, B, a, b, M):
	"""
	Cálcula la matriz de distancias a partir de 2 strings.
	Recursivo. Memoriza resultados intermedios.
	DINAMICO: TIEMPO POLINOMICO A*B
		A = Primer string
		B = Segundo string
		a = Largo de la cadena del string A
		b = Largo de la cadena del string B
		M = Matrix(a+1,b+1)
	"""
	if M[a][b] is not None:
		resultado = 0
	elif a == 0 or b == 0:
		resultado =  1
	elif A[a-1] == B[b-1]:
		resultado = 1 + EfficientLCS_Inst(A, B, a-1, b-1, M)
	else:
		resultado = 1 + EfficientLCS_Inst(A, B, a-1, b, M) + EfficientLCS_Inst(A, B, a, b-1, M)
	M[a][b] = not None
	return resultado

def BottomLCS_Inst(A, B):
	"""
	Cálcula la matriz de distancias a partir de 2 strings.
	Iterativo. Memoriza resultados previos.
	DINAMICO: TIEMPO POLINOMICO
		A = Primer string
		B = Segundo string
	"""
	resultado = 0
	len_A = len(A)
	len_B = len(B)
	M = Matrix(len_A+1, len_B+1)

	for a in range(len_A+1):
		for b in range(len_B+1):
			if a == 0 or b == 0:
				resultado += 1
				M[a][b] = 0
			elif A[a-1] == B[b-1]:
				resultado += 1
				M[a][b] = M[a-1][b-1]
			else:
				resultado += 1
				M[a][b] = max(M[a-1][b], M[a][b-1])

	return resultado


# str1 = 'AA'
# str2 = 'BB'
# print(NaiveLCS_Inst(str1, str2, len(str1),len(str2)))
# print(EfficientLCS_Inst(str1, str2, len(str1),len(str2), Matrix(len(str1)+1, len(str2)+1)))
# print(BottomLCS_Inst(str1, str2))