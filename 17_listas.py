numbers = [1,2,3,4,5]
frutas = ["banana", "manzana", "uva"]
print(f"Lista numeros -> {numbers}")
print(f"Solo del 1 al 3 -> {numbers[:3]}")
print(f"Lista frutas -> {frutas}")

print("*"*30)

num = input("Digite numero: ")
print(f"El numero {numbers[int(num) - 1]}")

print("*"*30)

frutas[0] = "pera"
print(frutas)
print('pera' in frutas)