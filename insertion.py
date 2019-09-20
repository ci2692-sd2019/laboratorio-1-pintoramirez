# 
# Fecha: 19-09-2019
# Integrantes: Daniel Pinto
#			   Daniela Ramirez
#
# Algoritmo de ordenamiento Insertion Sort

# Programa:

def InsertionSort(A:[int]):

	for i in range(1,len(A)):
		x = A[i]
		k = i-1

		while k>=0 and x<A[k]:
			A[k+1] = A[k]
			k -= 1

		A[k+1] = x

	return A 

