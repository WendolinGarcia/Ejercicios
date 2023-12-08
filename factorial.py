def factorial():
    # Pedir al usuario que ingrese un número
    n = int(input("Ingrese número: "))
    
    # Inicializar el factorial a 1
    f = 1

    # Calcular el factorial utilizando un bucle for
    for i in range(1, n + 1):
        f *= i

    # Mostrar el resultado
    print("El factorial de", n, "es:", f)

# Llamar a la función principal
factorial()
