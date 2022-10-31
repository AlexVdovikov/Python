'''N1v6 Дана целочисленная квадратная матрица. Найти в каждой строке
наибольший элемент и в каждом столбце наименьший. Вывести на
экран'''
import random
n=int(input("Введите кол-во столбцов и строк "))
A = [[random.randrange(1000) for i in range(n)] for j in range(n)]
print("Исходная матрица ")
for i in range(n):
	print(A[i])
imax = jmax = 0
rmax = []
cmin = A[0].copy()
amax = A[0][0]
for i in range(n):
	if A [i][i] > amax:
		imax = i
		jmax = i
		amax = A[i][i]
	if A[i][n-i-1] > amax:
		imax = i
		jmax = n-i-1
		amax = A[i][n-i-1]
	tmax= A[i][0]
	for j in range(n):
		if tmax < A[i][j]:
			tmax = A[i][j]
		if cmin[j] > A[i][j]:
			cmin[j] = A[i][j]
	rmax.append(tmax)
A[n//2][n//2], A[imax][jmax] =A[imax][jmax], A[n//2][n//2]
print('максимумы строк: ')
print(*rmax)
print('минимумы столбцов: ')
print(*cmin)
print()
for row in A:
	print(*map('{:>3d}'.format,row))
