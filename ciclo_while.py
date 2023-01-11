secret_number = 10
intento = int(input("Ingresa un numero entero: "))

if intento == secret_number:
    print("¡Bien hecho, muggle! Eres libre ahora.")
else:
    while intento != secret_number:
        print("¡Ja, ja! ¡Estás atrapado en mi bucle!")