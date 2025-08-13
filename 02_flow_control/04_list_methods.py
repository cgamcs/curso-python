###
# 04 - Listas Métodos
# Los métodos más importantes para trabajar con listas
###

from os import system
if system("clear") != 0: system("cls")

lista1 = ['a', 'b', 'c', 'd']

# Añadir o insertar elementos a la lista

lista1.append('e') # Añade un elemeno al final de la lista
print(lista1)

lista1.insert(1, '@') # Inserta un elemento en la posición que le indiquemos como primer argumento
print(lista1)

lista1.extend(['😁', '😍']) # Agrega elementos al final de la lista
print(lista1)

# Eliminar elementos de la lista

lista1.remove('@') # Elimina la primer aparición del elemento que le indiquemos
print(lista1)

ultimo = lista1.pop() # Elima el último elemento de la lista y además lo devuelve
print(ultimo)
print(lista1)

lista1.pop(1) # Elimina el segundo elemento de la lista (es el indice 1)
print(lista1)

# Eliminar a lo bruto
del lista1[-1]
print(lista1)

lista1.clear() # Eliminar todos los elementos de la lista
print(lista1)

# Eliminar un rango de elementos
lista1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

del lista1[1:3]
print(lista1)

# Más métodos útiles
print('Ordenar listas')
numbers = [3, 10, 2, 8, 99, 101]
numbers.sort()
print(numbers)

print('Ordenar listas creando una copia')
numbers = [3, 10, 2, 8, 99, 101]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

print("Ordenar una lista de cadenas de texto (todo minúsculas)")
frutas = ['manzana', 'pera', 'limón', 'manzana', 'pera', 'limón']
sorted_numbers = sorted(frutas)
print(sorted_numbers)

print("Ordenar una lista de cadenas de texto (mezcla de mayúsculas y minúsculas)")
frutas = ['manzana', 'Pera', 'Limón', 'manzana', 'pera', 'limón']
frutas.sort(key=str.lower)
print(frutas)

# Más cosas útiles
lista1 = ['a', 'b', 'c', 'd', 'b']

print(len(lista1)) # Tamaño de la lista -> 5
print(lista1.count('b')) # Cuantas veces aparece el elemento 'b' -> 2
print('e' in lista1) # Comprueba si hay una 'e' en la lista -> False