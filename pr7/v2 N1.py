'''v2 №1 Вычислить площадь правильного шестиугольника со стороной а, используя
подпрограмму вычисления площади треугольника.'''
a=int(input("а: "))
def s3(a):
	return (pow(3,0.5)*pow(a,2))/4
def s6(a):
	return 6*s3(a)
print(s6(a))