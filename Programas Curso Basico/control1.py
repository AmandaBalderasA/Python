# Programa que determina la estacion del anio dado el mes
mes = int(input("Ingresa el numero del mes: "))
estacion = ""
if mes == 12 or mes == 1 or mes == 2:
    estacion = "Invierno"
elif mes == 3 or mes == 4 or mes == 5:
    estacion = "Primavera"
elif mes == 6 or mes == 7 or mes == 8:
    estacion = "Verano"
elif mes == 9 or mes == 10 or mes == 11:
    estacion = "otonio"
else:
    print("Mes invalido")

print("Estacion del mes " + str(mes) + ": ", estacion)