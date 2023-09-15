# CRUD

# Create 
numbers = [1,2,3,4,5]
frutas = ["banana", "manzana", "uva"]

# Read
print(f"Numeros: {numbers}")
print(" ")
print("*"*30)

# Update
frutas[1] = 'pera'
frutas.append("papaya") # Lo agrega al final de la lista
frutas.insert(0,"mango") # Lo agrega donde quiera
frutas.insert(-1,2) # Puedo agregar un int en una lista
print(f"Frutas -> {frutas}")

print(" ")
print("*"*30)

new_list = frutas + numbers
print(f"Nueva lista de frutas y numeros{new_list}")
index = new_list.index(4) # Hay que tener muy en cuenta que diferencia entre strigns e ints
print(f"Posicion de 4 -> {index}")
index = new_list.index("papaya")
print(f"Posicion de papaya -> {index}")
new_list[index] = "guanabana"
print(f"Lista con guanabana -> {new_list}")

print(" ")
print("*"*30)

# Delete
new_list.remove("mango") # Remover uno especifico
print(f"Elimina Mango -> {new_list}")
new_list.pop() # Sacar el ultimo
print(f"Elimina el ultimo -> {new_list}")
new_list.pop(2) # Sacar uno especifico
print(f"Elimina uva -> {new_list}")

print(" ")
print("*"*30)

new_list.reverse() # Darle reversa a la lista
print(f"Lista al reverso -> {new_list}")

print(" ")
print("*"*30)


numerosSort = [1,4,9,7,2,3]
print(f"Numeros desordenados -> {numerosSort}")
numerosSort.sort()
print(f"Numeros ordenados -> {numerosSort}")
personas = ["Mario", "Juan", "Pablo", "Maria", "Ana"]
personas.sort()
print(f"Personas ordenadas -> {personas}")