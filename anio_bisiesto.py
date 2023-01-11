anio = int(input("Anio: "))
tipo = ""
if anio >= 1582:
    if anio % 4 != 0:
        print(anio, " es un anio comun")
    elif anio % 100 != 0:
        print(anio, " es un anio bisiesto")
    elif anio % 400 != 0:
        print(anio, " es un anio comun")
    else:
        print(anio, " es un anio bisiesto")
else:
    print("No dentro del período del calendario Gregoriano")
