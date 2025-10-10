# ***** JUGANDO CON CADENAS DE CARACTERES *****
# El presente codigo implementa la separacion de una sola cadena de caracteres a dos
# y almacenandolas en dos variables diferentes
# al mismo tiempo en que la cadena original se invierte el orden los caracteres

Mensaje = "Aprendiendo Python" #Cadena de caracteres original
#Division del "Mensaje" en dos variables diferentes 
Mensaje1 = Mensaje[:11] # Mensaje[:11] especifica que vas a tomar los caracteres de Mensaje desde que inicia hasta el caracter 11
Mensaje2 = Mensaje[12:] # Especifica que le va asignar a Mensaje2 partiendo desde el caracter 12 hasta el final
Invertido = Mensaje[::-1] # Asignas todo el contenido de mensaje pero -1 (al reves)

#Impresion en consola de resultados
print(Mensaje1)
print(Mensaje2)
print(Invertido)