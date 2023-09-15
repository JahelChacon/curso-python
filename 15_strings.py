text = "Sabe programar en Python"
print('Javascript' in text) # False
print('Python' in text) # True

size = len('amor  ')
sizeClear = len('amor')
print(size)
print(sizeClear)

print(f"{text} -> {text.upper()} -> {text.lower()}")
print(f"Contador de a -> {text.count('a')}")
print(f"Swap case, cambiar mayúsculas -> {text.swapcase()}")
print(text.startswith('Sabe')) # True
print(text.endswith('JS')) # False
print(f"Reemplazar por GO -> {text.replace('Python', 'GO')}")
print(f"Capitalize primera letra -> {text.capitalize()}")
print(f"Cada primera letra en mayúscula -> {text.title()}")
print(f"Ver si es un digito -> {text.isdigit()}") # False
print("35".isdigit()) # True
