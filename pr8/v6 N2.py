'''N6 zad2 дана действительная квадратная матрица порядка N (N — нечетное),
все элементы которой различны. Найти наибольший элемент среди
стоящих на главной и побочной диагоналях и поменять его местами с
элементом, стоящим на пересечении этих диагоналей.'''
import random
n=int(input("Введите кол-во столбцов и строк "))
A = [[random.randrange(1000) for i in range(n)] for j in range(n)]
for i in A:
	print(i)
print()

b = sum(A,[])
maximum1 = max(b[::n+1]) 
maximum2 = max(b[n-1::n+1][:n])
if maximum1 > maximum2:
	i=j=b[::n+1].index(maximum1)
else:
	i=b[n-1::n-1][:n].index(maximum2)
	j=n-1-i
A[n//2][n//2], A[i][j] = A[i][j], A[n//2][n//2]
for i in A:
	print(i)