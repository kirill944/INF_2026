# Вспомогательная таблица (решение все равно руками)

for x in range(2):
    for y in range(2):
        for z in range(2):
            f = x or y or z # Функция из условия
            print(x, y, z, '|', int(f)) # Если надо в другом порядке, менять здесь