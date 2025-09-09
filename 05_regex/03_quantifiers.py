###
# 03 - Quantifiers
# Los cuantificadores se utilizan para especificar cuántas ocurrencias de un carácter
# o gruo de caracteres se deben encontrar en una cadena.
###
from os import system
if system("clear") != 0: system("cls")

import re

# *: Puede aparecer 0 o más veces
text = "aaaba"
pattern = r"a*"
found = re.findall(pattern, text)
print(found)

# Ejercicio 1:
# ¿Cuántas palabras tienen de 0 a más "a" y despues una "b"
text = "¿Cuántas palabras tienen de 0 a más 'a' y despues una 'b'?"
pattern = r"a*+b"
found = re.findall(pattern, text)
print(found)

# +: Una o más veces
text = "dddd aaa ccc a bb casa"
pattern = r"a+"
found = re.findall(pattern, text)
print(found)

# ?: Cero o una vez
text = "aaabacb"
pattern = r"a?b"
found = re.findall(pattern, text)
print(found)

# Ejercicio 2:
# Haz opcional que aparezca un +34 en el siguiente telefono
text = "+0034 233823492"
pattern = r"\+(00)?34 \d{9}"
found = re.search(pattern, text)
print(found.group())

# {n}: Exactamente n veces
text = "aaaaaa         aa   aaaa"
pattern = "a{3}"
matches = re.findall(pattern, text)

print(matches)

# {n, m}: De n a m veces
text = "u uu uuu u"
pattern = r"\w{2,3}"
matches = re.findall(pattern, text)
print(matches)

# Ejercicio:
# Encuentra las palabras de 4 a 6 letras en el siguiente texto
words = "ala casa árbol león cinco murcielago"
pattern = r"\b\w{4,6}\b"
matches = re.findall(pattern, words)
print(matches)

# Ejercicio
# Encuentra las palabras de más de 6 letras
words = "ala fantastico casa árbol león cinco murcielago"
pattern = r"\b\w{6,}\b"
matches = re.findall(pattern, words)
print(matches)