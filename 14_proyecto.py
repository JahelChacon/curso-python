import random

user_option = input("Elige piedra, papel o tijera -> ")
option = random.randrange(1,4)
if option == 1:
    cpu_option = 'piedra'
elif option == 2: 
    cpu_option = 'papel'
else:
    cpu_option = 'tijera'

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