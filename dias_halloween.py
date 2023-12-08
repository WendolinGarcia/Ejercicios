from datetime import datetime, timedelta

def dias_para_halloween():
    # Pedir al usuario que ingrese la fecha actual
    dia_actual = int(input("Ingrese el día actual: "))
    mes_actual = int(input("Ingrese el mes actual: "))
    
    # Obtener la fecha actual
    fecha_actual = datetime.now()

    # Definir la fecha de Halloween
    fecha_halloween = datetime(fecha_actual.year, 10, 31)  # Octubre

    # Verificar si Halloween ya ocurrió este año
    if fecha_actual > fecha_halloween:
        fecha_halloween = datetime(fecha_actual.year + 1, 10, 31)  # Usar el próximo año

    # Calcular los días que faltan para Halloween
    dias_faltantes = (fecha_halloween - fecha_actual).days

    # Mostrar los días que faltan para Halloween
    print("Días que faltan para Halloween:", dias_faltantes)

# Llamar a la función principal
dias_para_halloween()
