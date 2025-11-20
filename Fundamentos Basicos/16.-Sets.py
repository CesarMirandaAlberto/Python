#-----------------------------------------------------------------------------------------
#                               **** SETS ****
# El presente código implementa el uso de SETS aplicando diferentes metodos
# El código simula un set de usuarios predefininidos y  un segundo set "ListadeEspera"
# Usuarios.add(Nuevo) para agregar un nuevo elemento en el set
# Usuarios.remove(EliminaA) para eliminar un elemento del set
# Usuarios.update(LEspera) "Acualizar el set" **** COMBINA DOS SETS DIFERENTES ****
# se implementan constantes a fin de evitar números mágicos en las opciones
# mediante condicional if se evaluan las opciones del usuario 
# se implementa bucle for para mostrar los elementos del set
#-----------------------------------------------------------------------------------------

#Definición de constantes
AGREGAR = 1
ELIMINAR = 2
ACTUALIZAR = 3
#Definición de sets
Usuarios = {"Ingrid", "Sara", "Omar", "Abigail", "Luis"}
LEspera = {"Gerardo", "Majo", "Israel"}

#Menu de opciones
print("Opciones")
print("1.- Agregar usuario")
print("2.- Eliminar usuario")
print("3.- Actualizar con lista de espera")
print("4.- Ninguna")

#Tomas de datos
Opcion = int(input("Ingresa una opcion: "))

#Evaluación de opción del usuario
if Opcion == AGREGAR:
    Nuevo = input("Ingresa el nuevo usuario: ")
    Usuarios.add(Nuevo)
elif Opcion == ELIMINAR: 
    EliminaA = input("Ingresa el usuario a eliminar: ")
    Usuarios.remove(EliminaA)
elif Opcion == ACTUALIZAR:
    Usuarios.update(LEspera)
else:
    print("!!Opcion incorrecta!!")

for i in Usuarios:
    print(i)