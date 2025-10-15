#        **** CICLO WHILE ****
# El presente código implementa el ciclo while
# El código simula que un sensor marca 45 grados y tiene que encender un ventilador
# mientras la temperatura disminuye al mismo tiempo que notifica como baja la temperatura
# y el estado (encendio o apagado) del ventilador.

# Definición de constantes
Temperatura = 45
TEMPERATURAPERFECTA = 25
#Ventilador apagado inicialmente
Ventilador = False

while Temperatura > TEMPERATURAPERFECTA:
    # El ventilador se enciende y empieza a disminuir la temperatura
    Ventilador = True
    Temperatura-=1
    if Ventilador == True: # Si se enciende el ventilador
        print("Ventilador encendido")
    
    print("Temperatura del invernadero: "+str(Temperatura))

# Fuera del ciclo
Ventilador = False
if Ventilador == False:
    print("Ventilador Apagado")