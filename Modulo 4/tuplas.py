# Usan parentesis
tuple_1 = (1, 2, 4, 8)

# Pero tambien se pueden escribir solo con comas
tuple_2 = 1., .5, .25, .125

# Cada elemento de una tupla puede ser de distinto tipo 
tuple_3 = "Cadena", 13, 12.45, "Python"

print(tuple_1)
print(tuple_2)
print(tuple_3)

# Tupla vacia 
empty_tuple = ()

# Cuando solo tienen un elemento, se le pone una coma
one_element_tuple_2 = 1., 

var = 123
t1 = (1, )
t2 = (2, )
t3 = (3, var)

t1, t2, t3 = t2, t3, t1
print(t1, t2, t3)
