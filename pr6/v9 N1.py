'''v9 zad1 Дан одномерный массив, состоящий из N вещественных элементов. Ввести
массив с клавиатуры. Найти и вывести минимальный по модулю элемент.
Вывести массив на экран в обратном порядке.'''
n=int(input('Введите длину массива '))
a=[]
for i in range(n):
	print('Введите ',i,'элемент')
	a.append(float(input()))
print('Исходный массив ',a)
a.reverse()
print('Преобразованный массив',a)