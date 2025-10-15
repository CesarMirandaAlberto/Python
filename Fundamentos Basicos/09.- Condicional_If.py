#           **** CONDICIONAL IF ****
# El presente código implementa el condicional if- elif- else
# el código simula que un alumno ingresa su promedio y en base a
# este mediante el condicional determine si es apto para una beca,
# examen de selección de alumnos para beca o no es apto para ninguna
# de las anteriores.

# Definición de constantes
APTO = 9
MEDIA= 8
NO_APTO= 7

# Petición del promedio al alumno
Promedio= float(input("Ingresa tu promedio general: "))

# Si es mayor o igual el promedio
if Promedio >= APTO:
    print("!!Eres apto para una beca!!")
elif Promedio >= MEDIA:# Si se encuentra en la media del promedio
    print("!No eres apto para una beca pero puedes aplicar para un examen de selección")
else: # Si no esta en ningua de las anteriores
    print("No eres apto para la beca ni para aplicar para un examen de selección ")