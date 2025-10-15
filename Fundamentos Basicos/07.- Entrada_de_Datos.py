# ***** ENTRADA DE DATOS DE USUARIO *****
# El presente código implementa la lectura de datos del teclado 
# y concatenandolo a un texto asignado desde el código

Mensaje=" Bienvenido a python" # Mensaje de bienvenida para concatenar

Nombre =input("Ingresa tu nombre: ") # Creamos una variable llamada Nombre, imprime texto en consola pidiendo el nombre y especificamos(input) que leeremos del teclado

Bienvenida=Nombre + Mensaje # Concatenamos en una nueva variable El nombre leido del teclado con el mensaje

print("!Hola! "+ Bienvenida) #Imprimimos en consola texto mas concatenacion de nombre y mensaje de bienvenida




# **** LEER DATOS NUMERICOS *****
# Un dato importante a tomar en cuenta es que al leer datos del teclado
# estos son interpretados como cadenas de caracteres por lo que si se
# leen datos numericos estos no podrán ser utilizados para operaciones
# por lo que para poder utilizarlos es necesario convertirlo al tipo de
# dato que se requiere

# ******* CASO DE PRUEBA *******

#matricula = input("Ingresa tu matricula ") #Descomentar para caso de prueba y la siguiente linea comentala y observa los cambios

matricula = int(input("Ingresa tu matricula ")) # Crea una variable y especifica que sera un dato int leido del teclado e imprime texto en consola solicitando el dato
matricula += 1 #Hacemos una simple suma para comprobar que el dato leido es un int 


print("Tu nueva matricula es: ", str(matricula))
