var = input("Digita y para salir: ")
while var != 'y':
    print('Intentalo de nuevo')
    var = input("Digita y para salir: ")
else: 
    print('Se ejecuta el codigo y termina')

counter = 0
while counter < 10: 
    counter += 1
    print(counter)

print('*'*30)

counter = 0
while counter < 20: 
    counter += 1
    print(counter)
    if counter == 15: # Si el contador es 15 entonces termine el while
        break

print('*'*30)

counter = 0
while counter < 20: 
    counter += 1
    print(counter)
    if counter < 17: # Si el contador es menor a 17 pase a la siguiente iteración y omita el print
        continue
    print("Hola")