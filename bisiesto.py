import calendar

def verificar_bisiesto():
    # Pedir al usuario que ingrese un año
    año = int(input("Ingrese un año: "))
    
    # Verificar si el año es bisiesto utilizando el módulo calendar
    if calendar.isleap(año):
        print("El año", año, "es bisiesto.")
    else:
        print("El año", año, "no es bisiesto.")

# Llamar a la función principal
verificar_bisiesto()
