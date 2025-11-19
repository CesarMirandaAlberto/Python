#-----------------------------------------------------------------------------
#           **** LISTA 2D ****
# El presente código implementa el uso de una lista 2D donde 
# se simula un teclado matricial 4 x 4 con números, letras y
# caracteres.
# NOTA: LAS POSICIONES PARTEN DESDE EL NÚMERO 0 
# Se imprime y posteriormente se pide al usuario acceder a un 
# elemento de la lista 2D, se leen las coordenadas del elemento 
# que desea el usuario mediante una sola entrada del teclado para
# lo cual se implementa
# map = Asigna valores a las variables
# .split() separa las cadenas de caracteres cuando se encuentra un espacio
#-----------------------------------------------------------------------------

# Creación de filas 
Fila1 = ["1", "2", "3", "A"]
Fila2=  ["4", "5", "6", "B"]
Fila3 = ["7", "8", "9", "C"]
Fila4 = ["*", "0", "#", "D"]

#Creación de Lista 2D Filas y Columnas
Teclado= [Fila1, Fila2, Fila3, Fila4]

#Impresión de lista 2D
for fila in Teclado:
    for Caracter in fila:
        print(Caracter, end=" ")
    print()

print("Matriz 4 x 4")

#pedir al usuario las cordenadas de un caracter
fn1, cn1 = map(int, input("Ingresa fila y columna : ").split())

print("Haz presionado ")
print(Teclado[fn1][cn1])