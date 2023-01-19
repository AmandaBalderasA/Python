# Programa que opera sobre una pila en tiempo de ejecucion
pila = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
repetir = True

def agregar(pila):
    elemento = int(input("Agrega el nuevo elemento: "))
    pila.push(elemento)
    return pila

def eliminar(pila):
    pila.pop()
    print("Se elino el ultimo elemento de la pila")
    return pila


while (repetir != False):
    print("Menu para una pila: ")
    print("1. Agregar elemento")
    print("2. Eliminar elemento")
    print("3. Imprimir pila")
    print("4. Salir")
    eleccion = int(input("Seleccione el numero de la opcion que quiere realizar: "))
    if eleccion == 1:
        print("\n----Funcion de agregar----\n")
        agregar(pila)
        repetir == True

    elif eleccion == 2:
        print("\n----Funcion de eliminar----\n")
        eliminar(pila)
        repetir == True

    elif eleccion == 3:
        print("Imprimir pila")
        print(pila)
        repetir == True

    elif eleccion == 4:
        repetir = False
        print("Vuelve pronto :)")

    else:
        print("Opcion no valida")
        repetir == True
