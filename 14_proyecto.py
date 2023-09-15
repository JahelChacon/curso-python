import random

tuplaOpciones = ('piedra', 'papel', 'tijera') # Tupla de opciones

user_option = input("Elige piedra, papel o tijera -> ") # El usuario digita
while not user_option in tuplaOpciones:
    print("Opcion no valida, eliga una valida")
    user_option = input("Elige piedra, papel o tijera -> ")
## option = random.randrange(1,4) # Otra forma de random
cpu_option = random.choice(tuplaOpciones)

print(f"Usuario -> {user_option} / CPU -> {cpu_option}")

print("*"*30)

if user_option == cpu_option:
    print("Empate")
## Piedra
elif user_option == 'piedra': 
    if cpu_option == 'papel':
        print("CPU gana")
    else:
        print("Usuario gana")
## Papel
elif user_option == 'papel':
    if cpu_option == 'piedra':
        print("Usuario gana")
    else:
        print("CPU Gana")
## Tijera
elif user_option == 'tijera':
    if cpu_option == 'piedra':
        print("CPU Gana")
    else:
        print("Usuario gana")