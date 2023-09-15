diccionario = {
    "Ana": 18, 
    "Juan": 20,
    "Pedro": 15,
    "Maria": 24
}

personas = {
    'nombre': 'Juan',
    'edad': 20,
    'deporte': 'futbol'
}
print(f"Primer diccionario -> {diccionario}")
print(f"Diccionario personas -> {personas}")
print(f"Edad de Juan -> {personas['edad']}")
print(f"Usando el get(valor) -> {personas.get('vallr')}") # No se cae el programa
print(f"Usando el get(edad) -> {personas.get('edad')}") # Usando get 