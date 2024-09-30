# Crea el diccionario informacion_personal
informacion_personal = {
    "nombre": "Maria Salcedo",
    "edad": 28,
    "ciudad": "España",
    "profesion": "Ingeniera en Telecomunicaciones"
}

# Accede al valor asociado con la clave "ciudad" y modifícalo
informacion_personal["ciudad"] = "España"

# Agrega una nueva clave-valor al diccionario que represente la "profesion" de la persona
informacion_personal["especialidad"] = "Gestion de datos y base de datos"

# Verifica si la clave "telefono" existe en el diccionario
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0554321098"

# Elimina la clave "edad" del diccionario
del informacion_personal["edad"]

# Imprime el diccionario actualizado
print(informacion_personal)