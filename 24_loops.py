matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(f"Campo [0][0]{matriz[0][0]}")
print(f"Campo [1][2]{matriz[1][2]}")

for element in matriz:
    print(f"Imprime el campo matriz -> {element}")
    for item in element:
        print(f"Imprime el número -> {item}")