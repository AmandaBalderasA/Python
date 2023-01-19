# Usan parentesis
tuple_1 = (1, 2, 4, 8)

# Emplear la funcion len
print("Longitud de la tupla tuple_1: ", len(tuple_1))

# Pero tambien se pueden escribir solo con comas
tuple_2 = 1., .5, .25, .125

# Cada elemento de una tupla puede ser de distinto tipo 
tuple_3 = "Cadena", 13, 12.45, "Python"

print(tuple_1)
print(tuple_2)
print(tuple_3)

# Tupla vacia 
empty_tuple = ()
print(type(empty_tuple))

# Cuando solo tienen un elemento, se le pone una coma
one_element_tuple_2 = 1., 

var = 123
t1 = (1, )
t2 = (2, )
t3 = (3, var)

t1, t2, t3 = t2, t3, t1
print(t1, t2, t3)

# Si se elimina la coma, Python crea una variable, no una tupla

# Se pueden acceder a los elementos de la tupla al indexarlos
my_tuple4 = (1, 2.0, "cadena", [3, 4], (5, ), True)
print(my_tuple4[3])    # salida: [3, 4]

# Tambien se puede borrar toda la tupla
del tuple_1
# print(tuple_1)

# Igual se puede crear una tupla usando tuple()
# Es util para convertir un iterable (listas, cadenas, etc)
my_list = [2, 4, 6]
print("Mi lista: ", my_list) # salida: [2, 4, 6]
print("Tipo: ")
print(type(my_list)) # salida: <class 'list'=""></class>
tup = tuple(my_list)
print("Mi tupla", tup) # salida: (2, 4, 6)
print("Tipo: ")
print(type(tup)) # salida: <class 'tuple'=""></class>