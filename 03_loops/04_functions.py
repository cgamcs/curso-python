###
# 04 - Funciones
# Bloques de código reutilizables y parametrizables para hacer tareas especificas.
###

from os import system
if system("clear") != 0: system("cls")

""" Definición de una función

def nombre_de_la_función(parametro1, parametro2, ...):
  # docstring
  # cuerpo de la función
  return valor_de_retorno # opcional

"""

# Ejemplo de una función para imprimir algo en consola
def saludar():
  print("Hola!")

saludar()

# Ejemplo de una función con parémetro
def saludar_a(nombre):
  print(f"Hola {nombre}!")

saludar_a("César")
saludar_a("Janeth")
saludar_a("Daniela")
saludar_a("Miryam")
saludar_a("Polo")
# El parametro es lo que acepta la función
# El argumento es lo que se le pasa a la función

# Funciones con más parametros
def sumar(a, b):
  suma = a + b
  return suma

result = sumar(2, 3)
print(result)

# Documentar las funciones con docstring
def restar(a, b):
  """Resta dos números y devuelve el resultado"""
  resta = a - b
  return resta

print(restar.__doc__)

# Parámetros por defecto
def multiplicar(a, b = 2):
  return a * b

print(multiplicar(2))
print(multiplicar(2, 6))

# Argumentos por posición
def describir_persona(nombre, edad, sexo):
  print(f"Soy {nombre}, tengo {edad} años y  me identifico como {sexo}")

# Parámetros posicionales
describir_persona("César", 21, "pez")
describir_persona("Hombre", "Daniela", 19)

# Argumentos por clave
# Parámetros nombrados
describir_persona(sexo="pez", nombre="César", edad=21)
describir_persona(sexo="Hombre", nombre="Daniela", edad=19)

# Argumentos de longitud de variable (*args)
def sumar_numeros(*args):
  suma = 0
  for numero in args:
    suma += numero
  return suma

print(sumar_numeros(1, 2, 3, 4, 5))
print(sumar_numeros(1, 2))
print(sumar_numeros(1, 2, 3, 4, 5,6, 7, 8, 9, 10))

# Argumentos de clave-valor variable (**kwargs)
def mostrar_informacion_de(**kwargs):
  for clave, valor in kwargs.items():
    print(f"{clave}: {valor}")

mostrar_informacion_de(nombre="César", edad=21, sexo="pez")

print("\n")

mostrar_informacion_de(nickname="Janeth", is_rich=True, country="México")