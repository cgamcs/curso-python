###
# 01 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de código solo si se cumplen ciertas condiciones.
###

from os import system
if system("clear") != 0: system("cls")

print("Sentencia simple condicional")

age = 18
if age >= 18:
  print("Eres mayor de edad")

age = 15
if age >= 18:
  print("Eres mayor de edad")

print("\nSentencia condicional con else")

age = 16
if age >= 18:
  print("Eres mayor de edad")
else:
  print("Eres menor de edad")

print("\nSentencia condicional con else")

nota = 7
if nota >= 9:
  print("Sobresaliente")
elif nota >= 7:
  print("Notable")
elif nota >= 5:
  print("Aprobado")
else:
  print("Suspenso")

print("\nCondicionales múltiples")

edad = 16
tiene_licencia = True

if edad >= 18 and tiene_licencia:
  print("Puedes conducir")
else:
  print("No puedes conducir")

if edad >= 18 or tiene_licencia:
  print("Puede conducir")
else:
  print("No puede conducir")

es_fin_de_semana = False

if not es_fin_de_semana:
  print("Hay que trabajar")

print("\nAnidar condicionales")
edad = 21
tiene_dinero = False

if edad >= 18:
  if tiene_dinero:
    print("Puedes comprar una cerveza")
  else:
    print("Quedate en casa")
else:
  print("No puedes comprar una cerveza")

# Más facil de leer con elif
# if edad < 18:
#   print("No puedes comprar una cerveza")
# elif tiene_dinero:
#   print("Puedes comprar una cerveza")
# else:
#   print("Quedate en casa")

print("\nCondiciones con booleanos")
numero = 5
if numero:
  print("El número no es cero")

numero = 0
if numero: # False
  print("El número es cero")

nombre = "César"
if nombre:
  print("El nombre no está vacío")

nombre = ""
if nombre: # False
  print("El nombre esta vacío")

numero = 3 # Asignación
es_el_tres = numero == 3 # Comparación

if es_el_tres: # True
  print("El número es 3")

print("\nLa condición ternaria")
# Es una forma concisa de un if-else en una línea de código
# [código si cumple la condición] if [condición] else [código si no cumple la condición]

edad = 16
mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"

print(mensaje)

###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales
print("\nEjercicio 1:")
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

if num1 > num2:
  print(f"{num1} es mayor que {num2}")
elif num2 > num1:
  print(f"{num1} es menor que {num2}")
else:
  print("Ambos son iguales")

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)
print("\nEjercicio 2:")

num1, operacion, num2 = input("Introduzca una operación entre dos números separedos por espacios:\n").split()

num1 = int(num1)
num2 = int(num2)

if operacion == '+':
  print("Resultado: ", num1 + num2)
elif operacion == '-':
  print("Resultado: ", num1 - num2)
elif operacion == '*':
  print("Resultado: ", num1 * num2)
elif operacion == '/':
  if num2 == 0:
    print("Error")
  else:
    print("Resultado: ", num1 / num2)

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.
print("\nEjercicio 3:")

year = input("Introduzca un año: ")

year = int(year)

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
  print(f"{year} es un año bisiesto")
else:
  print(f"{year} no es un año bisiesto")

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)
print("\nEjercicio 4:")

edad = input("Introduzca su edad: ")

edad = int(edad)

if 0 <= edad <= 2:
  print("Bebé")
elif 3 <= edad <= 12:
  print("Niño")
elif 13 <= edad <= 17:
  print("Adolescente")
elif 18 <= edad <= 64:
  print("Adulto")
elif edad >= edad:
  print("Adulto mayor")
else:
  print("Edad no valida")