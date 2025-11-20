#-----------------------------------------------------------------------------
#                               **** TUPLAS ****
# El presente código implementa el uso de tuplas a fin de comprender la
# diferencia entre tuplas y listas.
# El ejercicio simula los datos de usarios y se implementa:
# Busqueda de un dato cualquiera mediante condicional if
# Usuarios.index(NUsuario): determinar la posición del dato
# Usuarios.count(NUsuario): contar las veces que se repite el dato
# Para todo esto se implementa print para mostrar los resultados 
#-----------------------------------------------------------------------------

#Declaración de tupla
Usuarios = ('Ingrid', 21, 'M','Omar', 27, 'H', 'Ingrid', 21, 'M', 'Luis', 24, 'M', 'Sara', 43, 'M')

#Pedir dato al usuario
NUsuario = input("Ingresa tu nombre de usuario: ")

#Busqueda del dato
if NUsuario in Usuarios:
    print("Usuario encontrado en la posicion")
    print(Usuarios.index(NUsuario))
    print("!Hay " + str(Usuarios.count(NUsuario)) + " mas con el mismo nombre!")
else:
    print("!!Usuario no encontrado!!")

