c0 = 15 #int(input("Ingresa un numero entero: "))
pasos = 0
if c0 < 1:
    print("No se aceptan valores negativos ni el cero")
else:
    while c0 != 1:
        if c0 % 2 == 0:
            c0 /= 2
        else:
            c0 = c0*3 + 1
        pasos += 1
        print(c0)

print("Pasos: ", pasos)
