'''var 13 zad 1 Дан одномерный массив целых чисел. Проверить, есть ли в нем одинаковые
элементы. Вывести эти элементы и их индексы.'''
from random import*
a=[randint(1,10)for i in range(15)]
b=[True for x in a ]
for i,x in enumerate(a):
	if b[i]:
		c=[j for j,y in enumerate(a) if x == y]
		if len(c) > 1:
			print(x,c)
			for j in c:
				b[j] = False