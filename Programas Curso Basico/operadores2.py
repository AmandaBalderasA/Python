# Programa que calcula area y perimetro de un rectangulo
altura = int(input("Ingrese altura del rectangulo: "))
ancho = int(input("Ingrese ancho del rectangulo: "))

area = altura * ancho
perimetro = 2*(ancho + altura) 
print("El area es: ", area)
print("El perimetro es: ", perimetro)