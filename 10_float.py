x = 3.3
y = 1.1 + 2.2
print("X -> ", x)
print("Y -> ", y)
print(x == y) # False

# Funcion format
y_String = format(y, ".2g") # Solo tener 2 digitos
print("String de Y -> ",y_String)

x_String = format(x, ".2g")
print("String de X -> ",x_String)
print(x_String == y_String) # True

# Forma 2
print("*"*20)

tolerance = 0.00001
print(abs(x-y) < tolerance) # True