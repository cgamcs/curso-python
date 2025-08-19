###
# 02 - Bucles (for)
# Permiten ejecutar un bloque de código repetidamente mientras ITERA un iterable o una lista
###

from os import system
if system("clear") != 0: system("cls")


# Iterar una lista
print("\nBucle for:")
frutas = ["manzana", "pera", "mandarina"]
for fruta in frutas:
  print(fruta)

# Iterar sobre cualquier cosa que sea iterable
print("\nBucle for con iterable:")
cadena = "midudev"
for caracter in cadena:
  print(caracter)

# enumerate()
print("\nBucle for con enumerate:")
frutas = ["manzana", "pera", "mandarina"]
for index, fruta in enumerate(frutas):
  print(f"El índice es {index} y la fruta es {fruta}")

# break
print("\nBucle for con break:")
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
for idx, animal in enumerate(animales):
  print(animal)

  if animal == "loro":
    print(f"El loro esta escondido en el índice {idx}")
    break

# continue
print("\nBucle for con continue:")
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
for idx, animal in enumerate(animales):
  if animal == "loro":
    continue

  print(animal)

# Comprension de listas (list comprehension)
print("\nBucle for con list comprehension:")
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
animales_mayus = [animal.upper() for animal in animales]

print(animales_mayus)

# Muestra los números pares de una lista
pares = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]
print(pares)