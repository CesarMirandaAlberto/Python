#-----------------------------------------------------------------------------
#        ***** DATOS NUMERICOS *****
#    El presente código implementa el uso de datos numericos 
#    en conjunto con cadenas de caracteres
#-----------------------------------------------------------------------------


NumeroLista = 12 #Variable de tipo entero
Promedio = 9.23 #Variable de tipo flotante
Nombre = "Alumno tu promedio es "

Mensaje = Nombre + str(Promedio) #se convierte el promedio que es un dato numerico a cadena de caracteres

#Mensaje = Nombre + Promedio #descomenta para caso de prueba y comenta la linea anterior     

#     Dado que no se puede sumar o concatenar dos tipos de datos diferentes 
#     el promedio(dato numerico) debe de ser convertido a cadena de caracteres
#     de lo contrario daria error.

#                                **** CASO DE PRUEBA ****
#    Para probar que marca errores descomenta la linea 13 para comprobar

print("Hola "+ Mensaje)
