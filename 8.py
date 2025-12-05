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
    u1 = s.count("Г")

    # Условие 2
    if "ГГ" in s:
        u2 = False
    else:
        u2 = True

    # Если все условия соблюдаются, печатаем слово и его номер
    if u1 >= 2 and u2:
        print(i + 1, s)