''' v4 zad2 Дан одномерный массив целого типа. Получить другой массив, состоящий
только из нечетных чисел исходного массива или сообщить, что таких чисел нет.
Полученный массив вывести в порядке убывания элементов.'''
from random import*
n=int(input())
a=[randint(1,2315)for i in range(n)]
b=[]
print('Исходный массив ' ,a)
for i in range (n):
	if a[i]%2!=0:
		b.append(a[i])
if len(b)==0:
	print('Нет нечетных чисел ')

b.reverse()
print(b)