'''N1v1 Вычислить сумму и число положительных элементов матрицы A[N, N],
находящихся над главной диагональю'''
import random
n=int(input("Введите кол-во столбцов и строк "))
k = 0
s = 0
A = [[random.randrange(1000) for i in range(n)] for j in range(n)]
for i in range(n):
	print(A[i])
for i in range(n):
	for j in range(i+1, n):
		if A[i][j] <= 0:
			continue
		if A[i][j] > 0:
			k +=1
			s += A[i][j]
print("Сумма ",s)
print("Число ", k)