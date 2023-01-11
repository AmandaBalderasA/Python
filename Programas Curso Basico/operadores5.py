# Programa que calcula el radio de una esfera
import math
radio = int(input("Ingresa el radio de la esfera: "))
volumen = (4/3) * math.pi * pow(radio, 3)

print("El volumen es: ", volumen)