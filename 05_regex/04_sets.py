from os import system
if system("clear") != 0: system("cls")

import re

# []: Coincide con cualquier caracter dentro de los corchetes
username = "rub.$ius_69+"
pattern = r"^[\w.%+-]+$"
match = re.search(pattern, username)
if match: print(match.group())
else: print("No es valido")

# Ejercicio:
# Buscar todas las vocales de una palabra
text = "Hola Mundo"
pattern = r"[aeiou]"
matches = re.findall(pattern, text)
print(matches)

# Una Rehex para encontrar las palabras man, fan y ban
# pero ingnora el resto
text = "man ran fan ñan ban"
pattern = r"[mfb]an"
matches = re.findall(pattern, text)
print(matches)

# Ejercicio:
# Nos han complicado el asunto, porque ahora hay palabras que encajan pero no empiezan
# por esas letras. Solo queremos las palabras man, fan y ban
text = "omniman fanatico man bandana"
pattern = r"\b[mfb]an\b"
matches = re.findall(pattern, text)
print(matches)

# Ejercicio final con todo lo aprendido
# Mejorar esto: https://www.computerhope.com/jargon/r/regular-expression.png

## Buscar corner cases que no pasa y arreglarlo:
# "lo.que+sea@shopping.online"
# "michael@gov.co.uk"
email = "michael@gov.co.uk"
pattern = r"[\w._%&+-]+@[\w.-]+\.[a-zA-Z]{2,6}"
match = re.search(pattern, email)
if match: print(f"Si es valido {match.group()}")
else: print("No es valido")

# [^]: Coincide con cualquier caracter que no esté dentro de los corchetes
text = "Hola mundo"
pattern = r"[^aeiou]"
matches = re.findall(pattern, text)
print(matches)