#-----------------------------------------------------------------------------
#           **** LISTAS ****
# El presente código implementa el uso de listas aplicadas a
# cadenas de caracteres donde se simula tener una lista de usuarios
# y se da la opción de Agregar o eliminar un usuario nuevo asi como
# ordenar la lista.
# 1.- AGREGAR: se implementa la función .append()
# 2.- ELIMINAR : se implementa la función .remove()
# 3.- ORDENAR : se implementa la función .sort()
# * Se implementan constantes a fin de evitar números mágicos
#-----------------------------------------------------------------------------

# Creacion de lista
Usuarios = ['Omar', 'Sara', 'Gerardo', 'Ingrid']

# Constantes
AGREGAR = 1
ELIMINAR = 2
ORDENAR = 3

#Menú de opciones
print("Selecciona tu opcion")

print("1.- Agregar usuario")
print("2.- Eliminar usuario")
print("3.- Ordenar lista")

Opcion = int(input("Ingresa una opcion: "))

# Condicionales que modifican la lista según la opción escogida
if Opcion == AGREGAR:
    Nuevo = input("Ingresa el nuevo usuario: ")
    Usuarios.append(Nuevo)
elif Opcion == ELIMINAR:
    EliminaA = input("Ingresa el usuario a eliminar: ")
    Usuarios.remove(EliminaA)
elif Opcion == ORDENAR:
    Usuarios.sort()
else:
    print("Opcion Incorrecta")

#Imprimir la lista
for i in Usuarios:
    print(i)