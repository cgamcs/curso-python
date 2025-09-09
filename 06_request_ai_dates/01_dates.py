# Trabajando con fechas y horas de Python

from os import system
if system("clear") != 0: system("cls")

from datetime import datetime, timedelta

# 1. Obtener la fecha y hora actual
now = datetime.now()
print(f"Fecha y hora actual {now}")

# 2. Crear una fecha y hora específica
specific_date = datetime(2026, 5, 13)
print(f"Fecha específica {specific_date}")

# 3. Formatear fechas
# método strftime() para formatear fechas
# pasarle el objeto datetime y el formato especificado
format_date = now.strftime("%d/%m/%Y")
print(f"Fecha formateada {format_date}")

# 4. Operaiones con fechas (sumar/restar dias, minutos, horas, meses)
yesterday = datetime.now() - timedelta(days=1)
print(f"Ayer: {yesterday}")

tomorrow = datetime.now() + timedelta(days=1)
print(f"Mañana: {tomorrow}")

one_hout_after = datetime.now() + timedelta(hours=1)
print(f"Una hora después: {one_hout_after}")

# 5. Obtener componentes individuales de una fecha
year = now.year
print(year)

month = now.month
print(month)

# 6. Calcular la diferencia entre 2 fechas
date1 = datetime.now()
date2 = datetime(2026, 5, 13)
difference = date2 - date1
print(difference)

# 7. Fomatear fecha en español
import locale
locale.setlocale(locale.LC_TIME, 'es_MX.UTF-8')

format_date = now.strftime("%A, %d de %B de %Y")
print(f"Fecha formateada {format_date}")