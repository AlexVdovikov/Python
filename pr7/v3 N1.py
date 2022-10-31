'''v3 №1 Даны катеты двух прямоугольных треугольников. Написать функцию
вычисления длины гипотенузы этих треугольников. Сравнить и вывести какая из
гипотенуз больше, а какая меньше.'''
import math 
def treygolnik1(kat1, kat2):
	gipotenuza1 = math.sqrt(pow(kat1,2)+pow(kat2,2))
	print(gipotenuza1)
	return gipotenuza1
def treygolnik2(kat1, kat2):
	gipotenuza2 = math.sqrt(pow(kat1,2)+pow(kat2,2))
	print(gipotenuza2)
	return gipotenuza2
if treygolnik1(int(input("1 катет 1 т: ")), int(input("2 катет 1 т: "))) > treygolnik2(int(input("1 катет 2 т: ")), int(input("2 катет 2 т: "))):
	print("Гипотенуза 1 треугольника больше ")
else:
	print("Гипотенуза 2 треугольника больше ")