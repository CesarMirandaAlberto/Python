#---------------------------------------------------------------------------------------------
#                          **** DICCIONARIOS ****
# El presente código implementa el uso de diccionarios donde se simula el temario
# de una materia de señales.
# El código implementa lo siguiente:
# Temario.keys() ** Presenta unicamente las claves del diccionario **
# Temario.get(Clave, "Clave no encontrada")) ** Obtiene el contenido de una clave **
# Temario.pop(ClaveEl, None) ** Elimina datos del diccionario clave y contenido **
# ClaveNueva, NombreNuevo = Datos.split(",") ** Separa datos en dos al encotrar coma **
# Temario.update({ClaveNueva.strip() : NombreNuevo.strip()}) ** Agrega nuevo elemento **
#---------------------------------------------------------------------------------------------

#Creación de diccionario
Temario = {
    'FFT' : "Transformada Rapida de fourier",
    'DFT' : "Trasnformada Discreta de fourier",
    'DSP' : "Procesamiento Digital de Señales",
    'OFDM': "Multiplexacion por division de frecuencias ortogonales",
    'LTI' : ['Superposicion', 'BIBO ESTABLES','INESTABLES', 21, ]
}

print(Temario.keys())

Clave=input("Ingresa la clave del temario: ")
print(Temario.get(Clave, "Clave no encontrada"))

ClaveEl=input("Ingresa la clave del temario a eliminar: ")
Temario.pop(ClaveEl, None)

Datos= input("Ingresa la clave y nombre del nuevo temario separados por coma: ")
ClaveNueva, NombreNuevo = Datos.split(",")

Temario.update({ClaveNueva.strip() : NombreNuevo.strip()})

print("Actualizacion")
print(Temario.keys())
