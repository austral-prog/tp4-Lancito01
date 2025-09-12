def leap_year():
    y = int(input("Ingrese un año: "))
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        print(f"El año {y} es bisiesto")
    else:
        print(f"El año {y} no es bisiesto")
