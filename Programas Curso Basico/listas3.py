lista_enteros = [1, 2, 3, 4, 5]
lista_flotantes = [1.5, 2.5, 3.5, 4.5, 5.5]

nueva_lista = lista_enteros + lista_flotantes
# nueva_lista.sort(reverse=True)
nueva_lista = sorted(nueva_lista, reverse=True)

print("Lista ordenada de manera descendente: ", nueva_lista)