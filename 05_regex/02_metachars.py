###
# 02 - Meta caracteres
# Los metacarcteres son simbolos especiales con significados
# especificos en las expresiones regulares
###
from os import system
if system("clear") != 0: system("cls")

import re

# 1. El punto (.)
# Coincidir con cualquier caracter excepto una nueva linea

text = "Hola mundo, h0la de nuevo, h$la otra vez"
pattern = "H.la"

found = re.findall(pattern, text, re.IGNORECASE)

if found: print(found)

# --------------------------

text = "Hola mundo, h0la de nuevo, h$la otra vez"
pattern = r"H.la"

found = re.findall(pattern, text, re.IGNORECASE)

if found: print(found)

# Cómo usar la barra invertida para anular el significado especial de un símbolo
text = "Hola mundo. H0la de nuevo. H$la otra vez"
pattern = r"\."

found = re.findall(pattern, text)

if found: print(found)

# \d: coincide con cualquier dígito (0-9)
text = "El número de teléfono es 123456789"
pattern = r"\d{9}"

found = re.findall(pattern, text)

if found: print(found)

# Ejercicio: encontrar si hay un número de España en el texto gracia al prefijo +34
text = "Mi número de teléfono es +34 688989378 apúntalo vale?"
pattern = r"\+34 \d{9}"
found = re.search(pattern, text)
print(found.group())

# \w: Coincide con cualquier caracter alfanumerico (a-z, A-Z, 0-9, _)
text = "@$el_rubius_69/&%"
pattern = r"\w"
found = re.findall(pattern, text)
print(found)

# \s: Coincide con cualquier espacio en blanco (espacio, tabulación, salto de línea)
text = "Hola mundo\n¿Cómo estás?\t"
pattern = r"\s"
found = re.findall(pattern, text)
print(found)

# ^: Coincide con el principio de una cadena
username = "%423_name"
pattern = r"^\w"
valid = re.search(pattern, username)

if valid: print("El nombre de usuario es valido")
else: print("El nombre de usuario no es valido")

phone = "+34 78237230"
pattern = r"^\+\d{2,3} "
valid = re.search(pattern, phone)

if valid: print("El número de teléfono es valido")
else: print("El número de teléfono no es valido")

# $: Coincide con el final de una cadena
text = "Hola mundo"
pattern = r"mundo$"

valid = re.search(pattern, text)
if valid: print("La cadena es valida")
else: print("La cadena no es valida")

# EJERCICIO
# Valida que un correo sea gmail
text = "cgamcs@gmail.com"
pattern = r"^\w+@gmail.com$"

valid = re.search(pattern, text)
if valid: print("Es un correo gmail valido")
else: print("Es un correo no valido")

# EJERCICIO
# Tenemos una lista de archivos, necesitamos saber los nombres de los ficheros con extension .txt
files = "file1.txt file2.pdf midu-of.webp secret.txt"
pattern = r"\w+\.txt"

found = re.findall(pattern, files)
print(found)

# \b: Coincide con el principio o final de una palabra
text = "casa casada cosa cosas casada casa"
pattern = r"\bc.sa\b"

found = re.findall(pattern, text)
print(found)

# |: Coincidir con una opción u otra
fruits = "platano, manzana, aguacate, palta, pera, aguacate, aguacate"
pattern = r"palta|aguacate|p..a|\b\w{7}\b"

found = re.findall(pattern, fruits)
print(found)