###
# 03 - range()
# Permite crear una secuencia de números. Puede ser útil para for, pero no solo para eso
###

from os import system
if system("clear") != 0: system("cls")

print("\nrange():")

nums = range(10) # NO ES UNA LISTA
# Generando una secuencia de números del 0 al 9
for num in nums:
  print(num)

# range(inicio, fin)
print("\nrange(incio, fin):")
for num in range(5, 10):
  print(num)

# range(inicio, fin, paso)
print("\nrange(incio, fin, paso):")
for num in range(0, 10, 2): # 0, 2, 4, 6, 8
  print(num)

# range() negativos
print("\nrange() negativos:")
for num in range(-5, 0):
  print(num)

print("\n")

for num in range(10, 0, -1):
  print(num)

# Crear lista con range
print("\nListas con range():")
nums = range(10)
list_of_nums = list(nums)
print(list_of_nums)

# Loop con range
for _ in range(5):
  print(f"Vuelta {_}")