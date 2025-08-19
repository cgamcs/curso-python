###
# 01 - Bucles (while)
# Permiten ejecutar un bloque de código repetidamente mientras se cumpla una condición
###

from os import system
if system("clear") != 0: system("cls")

print("\nBucle while:")

# Bucle con una simple condición
contador = 0
while contador <= 5:
  print(contador)
  contador += 1 # es super importante para evitar un bucle infinito

# utilizando la palabra break, para romper el bucle
print("\nBucle while con break:")
contador = 0

while True:
  print(contador)
  contador += 1
  if contador == 5:
    break # sale del bucle

# continue, que lo hace es saltar esa iteración en concreto
# y continuar con el bucle
print("\nBucle con continue:")
contador = 0
while contador < 10:
  contador += 1

  if contador % 2 == 0:
    continue

  print(contador)

# else, esta condición cuándo se ejecuta?
print("\nBucle while con else:")
contador = 0
while contador < 5:
  print(contador)
  contador += 1
else:
  print("El bucle ha terminado")

# else, esta condición cuándo se ejecuta?
print("\nBucle while con else usando break:")
contador = 0
while contador < 5:
  print(contador)
  contador += 1
  break
else:
  print("El bucle ha terminado")

# pedirle al usario un número que tiene
# que ser positivo si no, no lo dejamos
numero = -1
while numero <= 0:
  numero = int(input("Escribe un número positivo:"))
  if numero <= 0:
    print("El número debe ser positivo. Intentalo otra vez")

print(f"El número que se a introducido es: {numero}")

numero = -1
while numero <= 0:
  try:
    numero = int(input("Escribe un número positivo:"))
    if numero <= 0:
      print("El número debe ser positivo. Intentalo otra vez")
  except:
    print("Lo que introduces debe ser un número")

print(f"El número que se a introducido es: {numero}")