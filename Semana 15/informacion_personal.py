# Crear un diccionario llamado informacion_personal con datos ficticios
informacion_personal = {
    "nombre": "Nelly Chimbo",
    "edad": 35,
    "ciudad": "Tena",
    "profesion": "Arquitecta"
}

# Modificar el valor de la clave "ciudad"
informacion_personal["ciudad"] = "Quito"  # Cambio de ciudad

# Modificar el valor de la clave "profesion"
informacion_personal["profesion"] = "Diseñadora de interiores"  # Nueva profesión

# Verificar si la clave "telefono" existe, si no, agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0995874384"  # Número ficticio

# Eliminar la clave "edad" porque no es necesaria
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario en formato vertical
print("Información Personal:")
print("----------------------")
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")


