"""
itertoools - библиотека для комбинаций
product('СЛОВО', repeat=КОЛИЧЕСТВО_БУКВ) - перестановки
"""

# Шаблонный код
from itertools import *

a = product("ЛЕГКО", repeat=6)
a = list(a)
a.sort()

for i in range(0, len(a), 1):
    s = ''.join(a[i])

    # Условие 1
    if s.count("Г") >= 2:
        u1 = True
    else:
        u1 = False

    # Условие 2
    if "ГГ" in s:
        u2 = False
    else:
        u2 = True

    # Если все условия соблюдаются, печатаем слово и его номер
    if u1 and u2:
        print(i + 1, s) # Обязательно +1, если список с 1 по условию!