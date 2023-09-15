# Debe ejecutarse porque es TRUE
if True: 
    print("Deberia ejecutarse")
else: 
    print("No deberia ejecutarse")

# NO Debe ejecutarse porque es FALSE
if False: 
    print("Deberia ejecutarse")
else: 
    print("No deberia ejecutarse")

print("*"*30)

# Pregunta
mascota = input("Tienes un perro o un gato? ")
if mascota == "perro": 
    print("Buen gusto")
else: 
    print("No está mal")

print("*"*30)

# Elif 

deporte = input("Que deporte practicas futbol o volleyball, o ninguno?")
if deporte == "futbol":
    print("Que bien!")
elif deporte == "volleyball":
    print("Me encanta el volleyball!")
else: 
    print("Que mal")
