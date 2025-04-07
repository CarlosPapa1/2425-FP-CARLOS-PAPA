# Escritura de Archivo de Texto

# Abrimos (o creamos) el archivo en modo escritura ('w')
archivo = open("my_notes.txt", "w")

# Escribimos tres líneas de notas personales
archivo.write("1. Python permite manejar archivos de forma eficiente.\n")
archivo.write("2. La función open() se usa para abrir archivos.\n")
archivo.write("3. Siempre debemos cerrar los archivos correctamente.\n")

# Cerramos el archivo después de escribir
archivo.close()

# Lectura de Archivo de Texto

# Abrimos el archivo en modo lectura ('r')
archivo = open("my_notes.txt", "r")

# Leemos el contenido línea por línea usando readline()
print("Contenido del archivo:")
linea = archivo.readline()  # Lee la primera línea

# Mientras haya líneas por leer
while linea:
    print(linea.strip())  # Imprimimos la línea eliminando saltos de línea al final
    linea = archivo.readline()  # Leemos la siguiente línea

# Cerramos el archivo después de leer
archivo.close()

