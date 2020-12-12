text = 'lorem ipsum dolor sit amet Python is awesome'

print(text)

# Tak można dostać się do dokumentacji metody dla obiektu
# print(dir(text))
# print(help(text.count))

# sprawdzanie ilości powtórzeń tekstu w tekście
print(text.count('a'))

# Rozpoczęcie dużą literą
print(text.capitalize())

# Rozpoczęcie każdego wyrazu dużą literą
print(text.title())

print(text.startswith('lorem'))
print(text.startswith('Lorem'))
print('python'.endswith('on'))

# Znajdowanie indeksu od ktorego zaczyna sie szukany string
index = text.find('sit')
print(text[index:])

