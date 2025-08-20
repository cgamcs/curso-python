###
# Ejercicios
# Volver a los ejercicios anteriores
# y convertirlos en funciones
# e intentar utilizar todos los casos y conceptos
# que hemos visto hasta ahora
###

from os import system
if system("clear") != 0: system("cls")

# Ejercicio 1: Imprimir números del 1 al 10
# Imprime los números del 1 al 10 (inclusive) usando un bucle for y range().
print("\nEjercicio 1:")
def imprimir_range(a, b):
  for numero in range(a, b):
    print(numero)

imprimir_range(1, 11)

# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2:")
def calcular_media(*args):
  lista = []
  for numero in args:
    lista.append(numero)
    
  suma = 0
  for numero in lista:
    suma += numero

  resultado = suma / len(lista)
  print(resultado)

calcular_media(10, 20, 30, 40, 50)