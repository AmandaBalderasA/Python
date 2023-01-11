# Programa que calcula operaciones
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

# Suma 
suma = num1 + num2 
print("La suma es: ", suma)

# Resta
print("La resta es: ", num2 - num1)

# Multiplicacion
print("La multiplicacion de " + str(num1) + " y " + str(num2) + " es: ", str(num1*num2))

# Division
print("La division es: ", num2/num1)

# Exponenciacion
exponente = num1**num2
print("La exponenciacion es: ", exponente)

# Division entera
div_entera = num2 // num1
print("La division entera es: ", div_entera)

# Modulo 
print("El modulo es: ", num2 % num1)


