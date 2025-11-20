#--------------------------------------------------------------------------------------
#       **** OPERADORES LOGICOS ****
# Este código implementa los operadores lógicos 
# El código simula la lectura de un sensor de temperatura y humedad en un inverdero
# donde si la temperatura y humedad cumplen con parametros determinados se activa el
# ventilador en caso contrario no se enciende
# nota: Para el ventilador True= Encendido False: Apagado
#--------------------------------------------------------------------------------------
# Definición de constantes
VENTILADOR = False
CALIENTE = 35
MHUMEDO = 90

#Petición de temperatura y humedad
Temperatura = float(input("Ingresa la temperatura: "))
Humedad = float(input("Ingresa la humedad: ")) 

#and da 1 (verdadero) solo si las dos variables son verdaderas 
if Temperatura >=CALIENTE and Humedad >=MHUMEDO: 
    VENTILADOR = not VENTILADOR # Niega el estado del ventilador (enciende)
    print("Estado del ventilador: " + str(VENTILADOR))
else:
   print("Estado del ventilador: " + str(VENTILADOR))
   