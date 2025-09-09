###
# 04 - Dictionaries
# Los diccionarios son colecciones de pares clave-valor
# Sirven para almacenar datos relacionados.
###

from os import system
if system("clear") != 0: system("cls")

# ejemplo tipico de diccionario
persona = {
  "nombre": "midudev",
  "edad": 25,
  "es_estudiante": True,
  "calificaciones": [7,8,9],
  "socials": {
    "twitter": "@midudev",
    "instagram": "@midudev",
    "youtube": "@midudev"
  }
}

# para acceder a los valores
print("Accediendo a los valores:")

print(f"Nombre: {persona["nombre"]}")
print(f"Calificacion: {persona["calificaciones"][2]}")
print(f"Instagram: {persona["socials"]["instagram"]}")

# cambiar valores al acceder
print("\nCambiando valores:")

persona["nombre"] = "César"
persona["socials"]["instagram"] = "@cgamcs"

print(persona)

# eliminar una propiedad
print("\nElimininando valor edad y es_estudiante:")

del persona["edad"]
es_estudiante = persona.pop("es_estudiante")
print(f"es_estudiante: {es_estudiante}")

print(persona)

# sobreescribir un diccionario con otro diccionerio
print("\nSobreescribiendo un diccionario con otro diccionerio:")
a = { "name": "midudev", "age": 25 }
b = { "name": "madeval", es_estudiante: True }

a.update(b)
print(a)

# comprobar si existe una propiedad
print("\nBuscando propiedad:")
print("nombre" in persona)

# obtener todas las keys
print("\nkeys:")

print(persona.keys())

# obtener todos los valores
print("\nvalues:")
print(persona.values())

# obtener tanto la key como el valor
print("\nitems:")
print(persona.items())