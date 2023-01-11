tope = int(input("Ingrese el numero hasta el que llegara la lista: "))
lista_impares = []
lista_pares = []

for numero in range(tope):
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

print("Lista de numeros pares: ", lista_pares)
print("Lista de numeros impares: ", lista_impares)