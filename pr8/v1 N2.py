'''N1v2 Дана матрица B[N, М]. Найти в каждой строке матрицы
максимальный и минимальный элементы и поменять их с первым и
последним элементами строки соответственно.'''
import random
n = int(input("Строки "))
m = int(input("Столбцы "))
A = [[random.randrange(1000) for i in range(n)] for j in range(n)]
print("Исходная матрица ")
for i in range(n):
	print(A[i])
print("Преобразованная матрица ")
print(*map(min,A[::2]))