# Capturar dos números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Comparar y mostrar el mayor
if num1 > num2:
    print("El mayor es: {num1}")
elif num2 > num1:
    print("El mayor es: {num2}")
else:
    print("Ambos números son iguales.")