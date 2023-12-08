def pares_impares():
    # Pedir al usuario que ingrese un número
    a = int(input("Por favor ingrese un número: "))
    
    # Verificar si el número es par o impar
    if a % 2 == 0:
        print(a, "es un número par")
    else:
        print(a, "es un número impar")

# Llamar a la función principal
pares_impares()
