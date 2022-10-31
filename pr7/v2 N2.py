'''v2 №2  Пользователь вводит две стороны трех прямоугольников. Вывести их
площади.'''
import math 
def pr(a,b):
	return a*b
Z=[]
for i in range(3):
	print("Введите стороны",i,"-го прямоугольника ")
	a=int(input("а: "))
	b=int(input("b: "))
	Z.append(pr(a,b))
for i in range(3):
	print("Площадь",i,"-го прямоугольника")