'''v3 №2 Преобразовать строку так, чтобы буквы каждого слова в ней были
отсортированы по алфавиту.'''
str = input("Введите строку ").lower().split(' ')
for i in range(len(str)):
	str[i] = ' '.join(sorted(str[i]))
print(''.join(str))