"""
Estructura:

my_dictionary = {
    key1: value1,
    key2: value2,
    key3: value3,
}
"""

# Se puede escribir asi 
dictionary = {
    "gato": "chat", 
    "perro": "chien",
    "caballo": "cheval"}

# O asi 
phone_numbers = {'jefe': 5551234567, 'Suzy': 22657854310}

# Vacio
empty_dictionary = {}

print("dictionary: \n", dictionary)
print("phone_numbers:\n", phone_numbers)
print("empty_dictionary:\n", empty_dictionary)

# Para acceder a un elemento:
# 1. Se puede hacer referencia a la clave

item1 = dictionary["gato"]
print("item1 de dictionary: ", item1)

# 2. O usando el metodo get
item2 = dictionary.get("perro")
print("item2 de dictionary: ", item2)

# Para cambiar el valor asociado a una clave especifica:
# Se puede hacer referencia a la clave del elemento
dictionary["caballo"] = "horse"
print(dictionary["caballo"])

# Agregar
empty_dictionary["Carlos"] = "Ramirez"
print("Agregando a diccionario vacio:\n", empty_dictionary)

# Eliminar
del empty_dictionary["Carlos"]
print("Eliminando del diccionario vacio:\n", empty_dictionary)

# Me quede en el punto 4 de diccionarios 

# Insertar usando update()

# Eliminar usando popitem()