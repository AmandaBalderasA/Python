# Crear una lista vacia 
beatles = []

# Agregar elementos a la lista
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

# Pedirle al usuario que agregue elementos
for i in range(2):
    nuevo = input("Agregue el nuevo elemento: ") # Stu Sutcliffe  Pete Best
    beatles.append(nuevo)

print("Lista: ", beatles)

del beatles[-1]
del beatles[-1]

beatles.insert(0, "Ringo Starr")

print("Lista al final: ", beatles)