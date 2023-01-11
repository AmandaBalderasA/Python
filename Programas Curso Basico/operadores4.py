# Programa que determina si la edad ingresada esta dentro del rango de 30 a 39
edad_usuario = int(input("Ingresa tu edad: "))
if edad_usuario >= 30 and edad_usuario <40:
    print("La edad " + str(edad_usuario) + " esta dentro del rango de edades de 30 y 39")
elif edad_usuario < 0:
    print("Eso es imposible!")
else:
    print("Edad no entra dentro del rango")