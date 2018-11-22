class LCS:
	@staticmethod
	def Matrix(numero_filas, numero_columnas):
		return [[None]*numero_columnas for i in range(numero_filas)]

	@staticmethod
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
			return 1 + LCS.NaiveLCS_Inst(A, B, a-1, b-1)
		return 1 + LCS.NaiveLCS_Inst(A, B, a-1, b) + LCS.NaiveLCS_Inst(A, B, a, b-1)

	@staticmethod
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
			resultado = 1 + LCS.EfficientLCS_Inst(A, B, a-1, b-1, M)
		else:
			resultado = 1 + LCS.EfficientLCS_Inst(A, B, a-1, b, M) + LCS.EfficientLCS_Inst(A, B, a, b-1, M)
		M[a][b] = not None
		return resultado

	@staticmethod
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
		M = LCS.Matrix(len_A+1, len_B+1)

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

	@staticmethod
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
		if a == -1 or b == -1:
			return 0
		elif A[a] == B[b]:
			return 1 + LCS.NaiveLCS(A, B, a-1, b-1)
		return max(LCS.NaiveLCS(A, B, a-1, b), LCS.NaiveLCS(A, B, a, b-1))

	@staticmethod
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
		if a == -1 or b == -1:
			result = 0
		elif M[a][b] is not None:
			return M[a][b]
		elif A[a] == B[b]:
			result = 1 + LCS.EfficientLCS(A, B, a-1, b-1, M)
		else:
			result = max(LCS.EfficientLCS(A, B, a-1, b, M), LCS.EfficientLCS(A, B, a, b-1, M))

		if a > -1 and b > -1:
			M[a][b] = result

		return result

	@staticmethod
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
		M = LCS.Matrix(len_A+1, len_B+1)

		for a in range(len_A+1):
			for b in range(len_B+1):
				if a == 0 or b == 0:
					M[a][b] = 0
				elif A[a-1] == B[b-1]:
					M[a][b] = M[a-1][b-1] + 1
				else:
					M[a][b] = max(M[a-1][b], M[a][b-1])
		return M[a][b]

	@staticmethod
	def Backtrack(M, A, B, a, b):
		"""
		Obtiene la LCS a partir de la matriz de distancias.
		"""
		if a == 0 or b == 0:
			return ""
		elif A[a-1] == B[b-1]:
			return A[a-1] + LCS.Backtrack(M, A, B, a-1, b-1)
		elif M[a, b-1] > M[a-1, b]:
			return LCS.Backtrack(M, A, B, a, b-1)
		return LCS.Backtrack(M, A, B, a-1, b)
