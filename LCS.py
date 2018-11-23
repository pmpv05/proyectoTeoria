class LCS:
	@staticmethod
	def Matrix(numero_filas, numero_columnas):
		return [[None]*numero_columnas for i in range(numero_filas)]

	@staticmethod
	def NaiveLCS_Inst(A, B, a, b):
		"""
			A = Primer string
			B = Segundo string
			a = Largo de la cadena A
			b = Largo de la cadena B
		"""
		if a == 0 or b == 0:
			return 1
		elif A[a-1] == B[b-1]:
			return 1 + LCS.NaiveLCS_Inst(A, B, a-1, b-1)
		return 1 + LCS.NaiveLCS_Inst(A, B, a-1, b) + LCS.NaiveLCS_Inst(A, B, a, b-1)

	@staticmethod
	def EfficientLCS_Inst(A, B, a, b, M):
		"""
			A = Primer string
			B = Segundo string
			a = Largo de la cadena A
			b = Largo de la cadena B
			M = Matrix(a+1,b+1)
		"""
		if M[a][b] is not None:
			return 0
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
			A = Primer string
			B = Segundo string
			a = Largo de la cadena del string A
			b = Largo de la cadena del string B
		"""
		if a == 0 or b == 0:
			return 0
		elif A[a-1] == B[b-1]:
			return 1 + LCS.NaiveLCS(A, B, a-1, b-1)
		return max(LCS.NaiveLCS(A, B, a-1, b), LCS.NaiveLCS(A, B, a, b-1))

	@staticmethod
	def EfficientLCS(A, B, a, b, M):
		"""
			A = Primer string
			B = Segundo string
			a = Largo de la cadena del string A
			b = Largo de la cadena del string B
			M = [a+1][b+1]
		"""
		if a == 0 or b == 0:
			result = 0
		elif M[a][b] is not None:
			return M[a][b]
		elif a == 0 or b == 0:
			result = 0
		elif A[a-1] == B[b-1]:
			result = 1 + LCS.EfficientLCS(A, B, a-1, b-1, M)
		else:
			result = max(LCS.EfficientLCS(A, B, a-1, b, M), LCS.EfficientLCS(A, B, a, b-1, M))
		return result

	@staticmethod
	def BottomLCS(A, B):
		"""
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

