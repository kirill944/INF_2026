# Функция проверки на простоту
def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return True

# Функция поиска всех делителей
def f_dels(x):
    dels = []
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            dels.append(i)
            dels.append(x // i)
    return list(set(dels))
