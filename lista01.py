from ipaddress import summarize_address_range

print ("......................")
print("Lista - sumar todos")
print("...................")
#solicitar un numero final de la lista
num1=int("ingresar el numero hasta 100")

#crea la lista desde 1 hasta el $num1
lista = list(range(1, num1+1))

#calcular la suma
resultado=sum(lista)

#imprimir el resultado
print(f"La suma de la lista hasta {num1} es {resultado}")