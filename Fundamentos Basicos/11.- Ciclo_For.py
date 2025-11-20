#-----------------------------------------------------------------------------
#           **** CICLO FOR ****
# El presente código implementa el ciclo for
# el código pide al usuario que tabla de multiplicar le gustaria
# calcular y mediante el ciclo for, esta es calculada.
#-----------------------------------------------------------------------------

# Petición de número del que le gustaria calcular su tabla de multiplicar
Numero = int(input("Ingresa la tabla que deseas calcular: "))

# Constante máxima en la que va a llegar el iterador del ciclo for
# NOTA: El numero máximo es 11 para calculara hasta el 10 dado que los iteradores comienzan desde el 0
Maximo = 11 
for i in range(Maximo): # Suma 1 en cada vuelta del ciclo for
    
    print(f"{Numero} x {i} = {Numero * i}") #Impresión de resultados
