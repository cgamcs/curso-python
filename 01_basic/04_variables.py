###
# 04 - Variables
# Las variables sirven para guardar datos en memoria.
# Python es un lenguaje de tipado dinámico y de tipado fuerte.
###

# Asigna una variable
# solo hace falta poner esto
my_name = "César"
# print(my_name)

age = 21
# print(age)

# age = 27
# print(age)

# Tipado dinámico: el tipo de dato se determina en tiempo de ejecución, que quiere decir?
# que no tienes que declararlo explicítamente
# name = "César"
# print(type(name))

# name = 27
# print(type(name))

# Tipado fuerte: Python no realiza conversiones de tipado automáticamente
# print(10 + "2")

# f-string (literal de cadena de formato)
print(f"Hola soy {my_name}, tengo {age + 5} años")

# Forma no recomendad de asignar variables
name, age, city = "César", 21, "Monterrey"

# Convenciones de nombres de variables
mi_nombre_de_variables = "ok" # snake_case
nombre = "ok"

MiNombreDeVariable = "ko" # CamelCase
minombredevariable = "ko" # lowerCamelCase

mi_nombre_de_variable_123 = "ok"

MI_CONSTANTE = 3.14 # UPPER_CASE -> constantes

# 123_variable = "ko"
# mi-variable = "ko"
# mi variable = "ko"

# True = False No puedes usar palabras reservadas como nombres de variables

# ['False', 'None', 'True', 'and', 'as', 'assert',
# 'async', 'await', 'break', 'class', 'continue',
# 'def', 'del', 'elif', 'else', 'except', 'finally',
# 'for', 'from', 'global', 'if', 'import', 'in', 'is',
# 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
# 'return', 'try', 'while', 'with', 'yield']

is_user_logged_in: bool = True
print(is_user_logged_in)

is_user_logged_in = 42
print(is_user_logged_in)