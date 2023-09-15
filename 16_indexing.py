text = 'Sabe python'
print(text[0], text[5])

print("*"*30)

# Indexing

# Ultimo caracter
print(text[len(text) -1])
print(text[-1]) # Decirle el ultimo

# Slicing 
print(text[0:4]) # De la posicion 0 a la 5
print(text[:4]) # De la posicion 0 a la 5
print(text[5:11]) # De la posicion 5 a la 11
print(text[5:]) # De la posicion 4 a la 11
print(text[:]) # Todo el string
print(text[0:7:1]) # Quiero imprimir del 0 al 7 con 1 salto
print(text[::2]) # Quiero imprimir todo con 2 saltos