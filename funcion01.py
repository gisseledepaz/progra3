print('....................')
print('Madeline De Paz')
print('codigo')
print('....................')



def positivo_negativo(num):

    if num > 0:
        return "El número es positivo"
    elif num < 0:
        return "El número es negativo"
    else:
        return "El número es 0"


num1 = int(input("ingrese un numero "))
print( positivo_negativo(num1))

