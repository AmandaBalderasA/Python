def is_year_leap(anio):
    resultado = None
    if anio >= 1582:
        if anio % 4 != 0:
            resultado = False
        elif anio % 100 != 0:
            resultado = True
        elif anio % 400 != 0:
            resultado = False
        else:
            resultado = True
    return resultado

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")
