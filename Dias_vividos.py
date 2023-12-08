def calcular_dias_vividos():
    # Obtener la fecha actual
    dia_actual = int(input("Ingresa el día actual con número: "))
    mes_actual = int(input("Ingresa el mes actual con número: "))
    año_actual = int(input("Ingresa el año actual con número: "))
    
    if mes_actual <= 2:
        a = año_actual - 1
        b = mes_actual + 12
    else:
        a = año_actual
        b = mes_actual

    c = a // 100
    e = 2 - c + (c // 4)

    f = int(a * 365.25)
    fecha_juliana_actual = int(f) + int(30.6001 * (b + 1)) + dia_actual + e - 1524.5

    # Obtener la fecha de nacimiento
    dia_nacimiento = int(input("Ingresa tu día de nacimiento con número: "))
    mes_nacimiento = int(input("Ingresa tu mes de nacimiento con número: "))
    año_nacimiento = int(input("Ingresa tu año de nacimiento con número: "))

    if mes_nacimiento <= 2:
        g = año_nacimiento - 1
        h = mes_nacimiento + 12
    else:
        g = año_nacimiento
        h = mes_nacimiento

    i = g // 100
    j = 2 - i + (i // 4)
    k = int(g * 365.25)
    fecha_juliana_nacimiento = int(k) + int(30.6001 * (h + 1)) + dia_nacimiento + j - 1524.5

    # Calcular la diferencia de días
    diferencia_dias = int(fecha_juliana_actual - fecha_juliana_nacimiento)

    print("Tienes", diferencia_dias, "días de vida.")

# Llamar a la función principal
calcular_dias_vividos()
