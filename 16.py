from sys import setrecursionlimit

setrecursionlimit(10000)
# Кеширование
a = [0] * 10000

def f(n):
    # Если есть в кеше
    if a[n] != 0:
        return a[n]

    # Если нет в кеше (из условия)
    if n >= 7000:
        a[n] = n
    if n < 7000:
        a[n] = f(n+2) + n + 3

    # Возвращаем
    return a[n]

print(f(52) - f(56))