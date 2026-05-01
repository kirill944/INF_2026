def game(n, s1, s2):
    # Игра до 42 камней
    if s1 + s2 <= 42:
        if n - 1 == 1:
            return False
        if n - 1 == 2:
            return False
        if n - 1 == 3:
            return True # Победный ход
    # Если ходов больше, чем нам надо
    if n > 3:
        return False

    # Ходы
    moves = [game(n + 1, s1 // 3, s2), game(n + 1, s1 // 2, s2), game(n + 1, s1, s2 // 3), game(n + 1, s1, s2 // 3)]

    # У проигравшего all, у победителя any
    # !!! ЕСЛИ ЕСТЬ СЛОВО "НЕУДАЧНЫЙ", оба any
    if n % 2 == 1:
        return any(moves)
    else:
        return all(moves)

for i in range(4, 301):
    # В первой куче 50, во второй от 4 до 300
    if game(1, 50, i):
        print(i)
