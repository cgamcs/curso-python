###
# 05 - Entrada de usuario (input()) - Versión simplificada
# La función inut() permite obtener datos del usuario a través de la consola.
###

name = input("Hola, ¿cómo te llamas?\n")

age = input(f"Hola {name}, ¿cuántos años tienes?\n")

print(f"{name}, dentro de 20 años tendras {int(age) + 20} años.")

print("Obtener múltiples valores a la vez")
country, city = input("¿En qué país y ciudad vives?\n").split(", ")

print(f"Vives en {city}, {country}.")