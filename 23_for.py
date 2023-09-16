frutas = ['manzana', 'banana', 'uva', 'papaya']
for x in frutas:
    print(x)

individuo = {
    'nombre': 'David',
    'edad': 20,
    'idiomas': ['ingles', 'espanol', 'portugues']
}

print('*'*30)

# Primera forma de hacerlo 
for key in individuo:
    print(key, '=>',individuo[key])

print('*'*30)

# Segunda forma 
for key, value in individuo.items():
    print(key, '=>',value)

print('*'*30)

personas = [
    {
        'nombre': 'David',
        'edad': 20
    },
    {
        'nombre': 'Pedro',
        'edad': 14
    },
    {
        'nombre': 'Juan',
        'edad': 45
    }
]

for persona in personas:
    print(f"Nombre: {persona['nombre']}, Edad: {persona['edad']}")