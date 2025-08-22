print('....................')
print('Madeline De Paz')
print('codigo')
print('....................')



def verificar_numero(num):
    if num > 0:
        return "El número es positivo"
    elif num < 0:
        return "El número es negativo"
    else:
        return "El número es 0"


# Ejemplo de uso
print(verificar_numero(10))   # El número es positivo
print(verificar_numero(-5))   # El número es negativo
print(verificar_numero(0))    # El número es 0

