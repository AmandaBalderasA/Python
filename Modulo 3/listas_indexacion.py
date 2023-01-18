# Indexacion
numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numbers) # Imprimiendo contenido de la lista original.

numbers[0] = 111
print("\nPrevio contenido de la lista:", numbers) # Imprimiendo contenido de la lista anterior.

numbers[1] = numbers[4] # Copiando el valor del quinto elemento al segundo elemento.
print("Nuevo contenido de la lista:", numbers) # Imprimiendo el contenido de la lista actual.

print("\nLongitud de la lista:", len(numbers))


# Eliminacion
del numbers[1]
print(len(numbers))
print(numbers)


# Indices negativos

numbers = [111, 7, 2, 1]
print(numbers[-1])
print(numbers[-2])

# Agregar elementos 
numbers.append(4)
print(len(numbers))
print(numbers)

numbers.insert(0, 222)
numbers.insert(1, 333)
print(len(numbers))
print(numbers)

# Crear una lista vacia 
my_list = []

for i in range(5):
    my_list.append(i + 1)
print(my_list)

suma = 0
for i in my_list:
    suma += i
print("Suma: ", suma)

# Cambiar posiciones
my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)

