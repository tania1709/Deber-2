# Escritura de Archivo de Texto
archivo = open("my_notes.txt", "w")  # Abrir archivo en modo escritura

# Escribe al menos tres líneas de notas personales
archivo.write("Nota 1: Recuerda tomar tus pastillas hoy.\n")
archivo.write("Nota 2: Las clases empiezan a las 7 am.\n")
archivo.write("Nota 3: No olvides hacer tus tareas.\n")

archivo.close()  # Cerrar archivo


# Lectura de Archivo de Texto
archivo = open("my_notes.txt", "r")  # Abrir archivo en modo lectura

# Lee el contenido del archivo línea por línea
linea = archivo.readline()
while linea:
    print(linea.strip())  # Muestra en la consola cada línea leída
    linea = archivo.readline()

archivo.close()  # Cerrar archivo

