string = 'Python programming language'

print(string)
print(string[0])
print(string[-1])

# wycinanie stringa po indeksach: name(start:stop) || name(start:) || name(:stop)
print(string[2:6])
print(string[4:])
print(string[:4])

print(string[-3:])

# wycinanie co druiego elementu
print(string[::2])

# wucinanie od końca
numbers = '1,2,3,4,5,6,7,8,9,0'
print(numbers[::2])
print(numbers[::-2])

# Sprawdzanie czy string jest w stringu
print('programming' in string)
print('something' in string)