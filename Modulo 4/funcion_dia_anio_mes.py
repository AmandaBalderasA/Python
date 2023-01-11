import funcion_dias_meses

def day_of_year(year, month, day):
    suma_dias = 0 
    if year < 1582 or month < 1 or month > 12 or day < 1 or day > 31:
        return None
    else:
        for i in range(month):
            suma_dias += funcion_dias_meses.days_in_month(year, i + 1)
        
        diferencia = funcion_dias_meses.days_in_month(year, month) - day
        total = suma_dias + diferencia
        return total


print(day_of_year(2000, 12, 31))
