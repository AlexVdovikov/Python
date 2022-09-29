f1=1
f2=1
n=input('Введите число чисел ряда Фиббоначи ')
n=int(n)
i=0
while i < n-2:
	fsum=f1+f2
	f1=f2
	f2=fsum
	i+=1
print('Значение ',f2) 
