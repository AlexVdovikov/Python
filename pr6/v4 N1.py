'''v4 zad1 Дан массив целых чисел. Найти максимальный элемент массива и его
порядковый номер'''
from random import*
a=[randint(1,406)for i in range(10)]
print(a.index(max(a)))
print(a)