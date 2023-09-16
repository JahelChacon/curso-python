import random

# Opciones
tuplaOpciones = ('piedra', 'papel', 'tijera') # Tupla de opciones

# Variables
puntosUsuario = 0
puntosCPU = 0
Rondas = 1
ganador = False

while ganador == False:

    print("*"*10)
    print("RONDA:", Rondas)
    print("*"*10)

    # Eleccion usuario
    user_option = input("Elige piedra, papel o tijera -> ") # El usuario digita
    while not user_option in tuplaOpciones:
        print("Opcion no valida, eliga una valida")
        user_option = input("Elige piedra, papel o tijera -> ")
    #####

    # Eleccion CPU
    cpu_option = random.choice(tuplaOpciones)
    ## option = random.randrange(1,4) # Otra forma de random
    #####

    # Imprime lo elegido
    print(f"Usuario -> {user_option} / CPU -> {cpu_option}")

    if user_option == cpu_option:
        print("Empate")
    ## Piedra
    elif user_option == 'piedra': 
        if cpu_option == 'papel':
            print("CPU gana")
            puntosCPU += 1
        else:
            print("Usuario gana")
            puntosUsuario += 1
    ## Papel
    elif user_option == 'papel':
        if cpu_option == 'piedra':
            print("Usuario gana")
            puntosUsuario += 1
        else:
            print("CPU Gana")
            puntosCPU += 1
    ## Tijera
    elif user_option == 'tijera':
        if cpu_option == 'piedra':
            print("CPU Gana")
            puntosCPU += 1
        else:
            print("Usuario gana")
            puntosUsuario += 1
    #####

    if puntosUsuario > 2 or puntosCPU > 2:
        ganador = True
        if puntosUsuario > 1: 
            print("EL USUARIO GANA!!!!!")
        else:
            print("LA CPU GANA!!!!!")
    else:
        print(f"Usuario: {puntosUsuario} / CPU: {puntosCPU}")
        Rondas += 1