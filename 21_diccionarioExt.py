persona = {
    'nombre': 'Mario',
    'apellido': 'Perez',
    'edad': 19,
    'idiomas': ['español', 'inglés'],
}

print(persona)

persona['edad'] = 20
print(persona)
persona['idiomas'].append('Portugues')
print(persona)

# Delete
del persona['edad'] # borrar edad
print(persona)
persona.pop('apellido') # Otra forma de borrar un atributo
print(persona)

# Agregar un nuevo atributo al diccionario
persona['edad'] = 19

print(persona.items())
print(persona.keys())
print(persona.values())